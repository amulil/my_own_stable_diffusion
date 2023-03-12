# my_own_stable_diffusion
 Setup Own Stable Diffusion

## config webui
- add WebUI repo to submodule
```bash
git submodule update --remote --merge https://github.com/AUTOMATIC1111/stable-diffusion-webui
```
- update WebUI repo
```bash
git submodule update --remote --merge
```
- clone repo
```bash
git clone --recurse-submodules <repository-url>
```

## download model

| Model name | Model version |
| --- | --- |
| Stable Diffusion | [1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.ckpt) |
| | |

```bash
cd stable-diffusion-webui
pip install -r requirements.txt
pip install tqdm
python script.py --help
```

## example
```bash
# 
```

## references

1. https://stable-diffusion-art.com/automatic1111-colab/
2. https://rentry.org/voldy#-novelai-setup-


