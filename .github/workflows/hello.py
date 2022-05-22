name: On Push Run

on: workflow_dispatch

env:
  DEVOPS_DIR: devops

jobs:
  hello-world:
    name: Hello world
    runs-on: ubuntu-latest
    steps:
    - name: Check-out devops repository
      uses: actions/checkout@v2
      with:
        repository: jcdan3/devops
        token: ${{ secrets.GITHUB_TOKEN }}
        path: ${{ env.DEVOPS_DIR }}

    - name: Hello World
      run: python ${{ env.DEVOPS_DIR }}/hello_world.py
      shell: sh
