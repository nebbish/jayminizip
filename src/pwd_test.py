import os
import click
import jayminizip
import zipfile
import tempfile

PWD = "wXGTZJ9L5CYOrvOaUvPH7Nh"
data_files = {
    "one.txt" : b"hello world!\n",
    "two.txt" : b"booya kada\n",
}

@click.command
@click.argument('password', default=PWD)
def cli(password):
    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        for (name,data) in data_files.items():
            paths.append(os.path.join(tmp, name))
            with open(paths[-1], 'wb') as f:
                f.write(data)

        dat = os.path.join(tmp, "tx.dat")
        jayminizip.compress_multiple(paths, [], dat, password, 9)

        with zipfile.ZipFile(dat, 'r') as zf:
            for (name, data) in data_files.items():
                dat_content = zf.read(name, password.encode())
                assert dat_content == data, f"{name}'s content from the zip did not match orig, zip content: {dat_content}"

    return 0

if __name__ == '__main__':
    cli()
