FROM mcr.microsoft.com/devcontainers/python:3.13

# The upstream image currently ships a Yarn APT source whose signing key is no
# longer valid. Remove it before devcontainer features run apt operations.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    /usr/share/keyrings/yarnkey.gpg \
    /etc/apt/keyrings/yarn.gpg \
 && find /etc/apt/sources.list.d -maxdepth 1 -type f -iname '*yarn*' -delete
