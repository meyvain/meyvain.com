# M. Mitchell Leverstone's portfolio website

Available online at [mitch.leverstone.me](https://mitch.leverstone.me).

## Development

First, make sure you have [`uv`](https://docs.astral.sh/uv/) installed.

To start working on this project:

    # Downloading the project from GitHub
    git clone git@github.com:meyvain/mitch.leverstone.me.git

    # Get into the project directory
    cd mitch.leverstone.me

    # Prepare the python virtual environment
    uv sync

After that, to work on the site locally on your computer regenerate the site and serve it:

    uv run pelican -rl

Now go to [localhost:8000](http://localhost:8000) in the browser to see your site (served from your computer, not from the web).

## git

    git pull # to be sure you have all the late work from other contributors

    git add

    git commit   # +name your changes

    git push

## Deployment

Deployment is done automatically using GitHub actions whenever changes are pushed to the repository.

### The nitty-gritty details

The `leverstone.me` domain is registered and managed by [NameCheap](https://www.namecheap.com/).
It points to [Cloudflare](https://cloudflare.com/) for SSL. [Tom](https://github.com/nagasak45) got access for these. Cloudflare defines a CNAME record to GitHub, where this site is hosted with GH pages, on the `gh-pages` branch of [github.com/meyvain/mitch.leverstone.me](https://github.com/meyvain/mitch.leverstone.me).
