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

## download model

| Model name | Model version |
| --- | --- |
| Stable Diffusion | [1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.ckpt) |
| | |

```bash
# Rename your .ckpt or .safetensors file file to "model.ckpt" or "model.safetensors", and place it in the /models/Stable-diffusionfolder or using link command to link file
ln -s [model_file] ./model.ckpt
```

## example

