
ARG VERSION=42

FROM registry.fedoraproject.org/fedora-minimal:$VERSION

RUN rm /etc/yum.repos.d/fedora-cisco-openh264.repo && \
    dnf -y up && dnf -y in --setopt=install_weak_deps=False \
            binutils \
            bsdtar \
            ccache \
            createrepo_c \
            distribution-gpg-keys \
            file \
            fuse-overlayfs \
            git-core \
            gnupg2 \
            jq \
            libabigail \
            mock \
            nosync \
            podman \
            python3-pyelftools \
            rpm-sign \
            rpmdevtools \
            rsync \
            tar \
            zstd && \
            dnf clean all && \
    useradd -M -G mock builduser && \
    setcap cap_setuid=ep /usr/bin/newuidmap && \
    setcap cap_setgid=ep /usr/bin/newgidmap
