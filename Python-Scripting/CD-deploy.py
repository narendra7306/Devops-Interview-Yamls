#!/usr/bin/env python3
import argparse 
import os 
import shutil
import subprocess
import yaml


def run(cmd,cwd=None):
    print(f"\n>>> {cmd}")
    subprocess.run(cmd,shell=True,cwd=cwd,check=True)

def generate_version(build_number):
    return f"v{int(build_number)}.0.0"

def clone_repo(repo_url, branch, directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    run(f"git clone -b {branch} {repo_url} {directory}")

def update_values_yaml(values_file, image_repo, image_tag):
    with open(values_file) as f:
        values=yaml.safe_load(f)
    values.setdefault("image",{})
    values["image"]["repository"]=image_repo
    values["image"]["tag"]=image_tag
    with open(values_file,"w") as f:
        yaml.safe_dump(values,f,default_flow_style=False)

def git_commit_push(repo_dir, tag):
    run('git config user.name "narendra7306"',cwd=repo_dir)
    run('git config user.email "narendrareddy0a3@gmail.com"',cwd=repo_dir)
    run("git add .",cwd=repo_dir)
    st=subprocess.run("git diff --cached --quiet",shell=True,cwd=repo_dir)
    if st.returncode!=0:
        run(f'git commit -m "Update image tag to {tag}"',cwd=repo_dir)
        run("git push origin master",cwd=repo_dir)
    else:
        print("No Helm changes detected.")

def configure_eks(cluster,region):
    run(f"aws eks update-kubeconfig --region {region} --name {cluster}")
    run("kubectl get nodes")

def deploy(release,chart,ns):
    run(f"helm upgrade --install {release} {chart} --namespace {ns} --create-namespace")
    run(f"kubectl rollout status deployment/{release} -n {ns} --timeout=300s")

def verify(ns):
    run(f"kubectl get pods -n {ns}")
    run(f"kubectl get svc -n {ns}")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repo-url",required=True)
    p.add_argument("--branch",default="master")
    p.add_argument("--php-image",required=True)
    p.add_argument("--mysql-image",required=True)
    p.add_argument("--build-number",required=True)
    p.add_argument("--frontend-values",default="frontend/values.yaml")
    p.add_argument("--backend-values",default="backend/values.yaml")
    p.add_argument("--eks-cluster",required=True)
    p.add_argument("--aws-region",required=True)
    p.add_argument("--namespace",default="default")
    p.add_argument("--frontend-release",default="php-app-frontend")
    p.add_argument("--backend-release",default="mysql-backend")
    args=p.parse_args()

    version=generate_version(args.build_number)
    repo_dir="helm-repo"
    clone_repo(args.repo_url,args.branch,repo_dir)
    update_values_yaml(os.path.join(repo_dir,args.frontend_values),args.php_image,version)
    update_values_yaml(os.path.join(repo_dir,args.backend_values),args.mysql_image,version)
    git_commit_push(repo_dir,version)
    configure_eks(args.eks_cluster,args.aws_region)
    deploy(args.backend_release,os.path.join(repo_dir,"backend"),args.namespace)
    deploy(args.frontend_release,os.path.join(repo_dir,"frontend"),args.namespace)
    verify(args.namespace)
    print(f"Deployment completed successfully. Version: {version}")

if __name__=="__main__":
    main()
