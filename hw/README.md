# EMLO Session 2_2




## Q2-Q6

Tasks:
- [x] Add CIFAR10 datamodule to the `lightning-hydra-template` repo
- [x] Integrate `timm` pretrained models
- [x] Include a build command inside Makefile
- [x] Train and evaluate the model using `train.py` and `eval.py` respectively
- [x] Build a docker image; the model should be trainable using `docker run ...`


Code:
The code is present inside the hw2 folder. Change to that directory before dunning these commands.

To train the model, run the following code. You need to install the requirements from `requirements.txt` assuming Python3.8.

```
python src/train.py experiment=timm.yaml trainer.max_epochs=1
```

To evaluate the trained model, run
```
d=$(ls -td -- ./logs/train/runs/* | head -n 1 | xargs basename)
python src/eval.py ckpt_path=logs/train/runs/$d/checkpoints/last.ckpt
```
(The first command gets the latest run date/time)


To build the docker image and run the training inside the docker image, run the following commands
```
docker build -t emlo_s2 .
docker run emlo_s2 python src/train.py experiment=timm.yaml trainer.max_epochs=1
```

This docker build can also be run via the `make` command.
```
make build
```

