# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:39:03.474201+00:00

Working directory: .

```text
$ python3 session21-python/scripts/small-cloud-lab.py 19 --terraform /tmp/campusfix-tools.FCoLVB/terraform
$ /tmp/campusfix-tools.FCoLVB/terraform init -no-color
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/aws versions matching "~> 6.0"...
- Installing hashicorp/aws v6.68.0...
- Installed hashicorp/aws v6.68.0 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
 
$ /tmp/campusfix-tools.FCoLVB/terraform fmt -check
main.tf
 
Traceback (most recent call last):
  File "/Users/rudraym/devops-heros/session21-python/scripts/small-cloud-lab.py", line 30, in <module>
    run("fmt", "-check")
    ~~~^^^^^^^^^^^^^^^^^
  File "/Users/rudraym/devops-heros/session21-python/scripts/small-cloud-lab.py", line 25, in run
    result.check_returncode()
    ~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 509, in check_returncode
    raise CalledProcessError(self.returncode, self.args, self.stdout,
                             self.stderr)
subprocess.CalledProcessError: Command '['/tmp/campusfix-tools.FCoLVB/terraform', 'fmt', '-check']' returned non-zero exit status 3.

```

Exit code: 1
