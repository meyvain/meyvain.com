# Meytal Mitchell Vainstub portfolio website

Available online at [mitch.leverstone.me](https://mitch.leverstone.me).

## Development

To start working on this project:

    # Downloading the project from GitHub
    git clone git@github.com:meyvain/mitch.leverstone.me.git

    # Get into the project directory
    cd mitch.leverstone.me

    # Prepare the python virtual environment
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt

When working on the project make sure you always activate the virtual environment (in *all* terminals):

    source env/bin/activate

After that, to work on the site locally on your computer regenerate the site and serve it:

    # In one terminal window
    make regenerate

    # In another terminal window
    make serve

Now go to [localhost:8000](http://localhost:8000) in the browser to see your site (served from your computer, not from the web).

## git

    git pull # to be sure you have all the late work from other contributors

    git add

    git commit   # +name your changes

    git push

## Deployment

To deploy first run:

    source env/bin/activate

then run:

    make github

### The nitty-gritty details

The `leverstone.me` domain is registered and managed by [NameCheap](https://www.namecheap.com/).
It points to [Cloudflare](https://cloudflare.com/) for SSL. [Tom](https://github.com/nagasak45) got access for these. Cloudflare defines a CNAME record to GitHub, where this site is hosted with GH pages, on the `gh-pages` branch of [github.com/meyvain/mitch.leverstone.me](https://github.com/meyvain/mitch.leverstone.me).
