FROM ubuntu:20.04

LABEL description="TripleBrainブログのDockerイメージ"

RUN apt-get update && \
    apt-get -y install git gcc g++ make zlib1g-dev ruby ruby-dev && \
    gem install jekyll bundler github-pages

COPY . /TripleBrain/

WORKDIR /TripleBrain/

CMD ["jekyll", "serve"]