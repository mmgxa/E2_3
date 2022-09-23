from torch import nn
from timm.models import create_model

class Timm(nn.Module):
    def __init__(
        self,
        input_size: int = 3072,
        output_size: int = 10,
        lin1_size: int = 256,
        lin2_size: int = 256,
        lin3_size: int = 256,
        model: str = 'resnet18'
    ):
        super().__init__()
    
        self.model_orig = create_model(
            model,
            num_classes=output_size,
            in_chans=3,
            pretrained=True,
            checkpoint_path='')
        modules = list(self.model_orig.children())
        self.model = nn.Sequential(*modules)

            
            

    def forward(self, x):
        batch_size, channels, width, height = x.size()

        # (batch, 1, width, height) -> (batch, 1*width*height)
        # x = x.view(batch_size, -1)

        return self.model_orig(x)


if __name__ == "__main__":
    _ = Timm()
