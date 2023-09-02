# Installation

```
# Install InsightFace
# https://github.com/deepinsight/insightface/tree/master/python-package

pip install insightface
pip install onnxruntime-gpu
pip install onnxruntime

# Download proper model
# https://www.reddit.com/r/midjourney/comments/13pnraj/please_reupload_inswapper_128onnx/
# and place it inside project directory:

drwxr-xr-x 7 cr0xd cr0xd      4096 Sep  2 01:54 .git
-rw-r--r-- 1 cr0xd cr0xd        19 Sep  2 01:50 .gitignore
-rw-r--r-- 1 cr0xd cr0xd 554253681 Aug 30 00:11 inswapper_128.onnx
drwxr-xr-x 2 cr0xd cr0xd      4096 Aug 30 01:10 .ipynb_checkpoints
-rw-r--r-- 1 cr0xd cr0xd      1343 Aug 31 18:32 main.py
-rw-r--r-- 1 cr0xd cr0xd       351 Sep  2 01:54 README.md
-rw-r--r-- 1 cr0xd cr0xd        14 Aug 29 21:09 .tool-versions

mkdir images
mkdir models
mkdir results

python3 main.py
```
