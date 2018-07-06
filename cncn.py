import click
import yaml

CONTEXT_SETTINGS = dict(
    default_map={'runserver': {'port': 5000}}
)

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-l', '--image-list', type=click.File('r'))
@click.argument('input', type=click.File('rb'))
def replace(image_list, input):
    content = input.read()
    registry = "hub.huwo.io/vendor/"

    for line in image_list:
        origin_name = line.strip()
        new_name = registry + origin_name.strip().replace("/", "-", 1)

        content = image_replace(origin_name, new_name, content)

    content = content.replace("docker.io/", "")
    click.echo(content)

if __name__ == '__main__':
    cli()

def image_replace(origin_name, new_name, content):
    return content.replace(origin_name, new_name)
