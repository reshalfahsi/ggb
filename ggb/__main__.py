import click
import platform
import cv2
import numpy as np
try:
    import urllib.request as urllib
except:
    import urllib

from ggb import GGB, ColorSpace
import ggb


def print_version(ctx: click.Context, param: click.Parameter, value: bool) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.echo(
        "Running GGB %s with %s %s on %s"
        % (
            ggb.__version__,
            platform.python_implementation(),
            platform.python_version(),
            platform.system(),
        )
    )
    ctx.exit()


@click.command()
@click.argument("image")
@click.option(
    "--output",
    type=str,
    default="ggb_image.png",
    help="Output to the GGB Image result file.",
    show_default=True,
)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Display the GGB version and exit.",
)
def main(
    image: str,
    output: str,
) -> None:
    img = None

    try:
        req = urllib.urlopen(image)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
    except:
        img = cv2.imread(image)

    ggb_image = GGB(image=img, input_color=ColorSpace.BGR).process()
    ggb_image.write(output)


if __name__ == "__main__":
    main()
