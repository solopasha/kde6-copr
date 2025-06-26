
ARG VERSION=42

FROM registry.fedoraproject.org/fedora-minimal:$VERSION

RUN rm /etc/yum.repos.d/fedora-cisco-openh264.repo && \
    curl -Ss -L https://copr.fedorainfracloud.org/coprs/solopasha/plasma-unstable/repo/fedora-42/solopasha-plasma-unstable-fedora-42.repo > /etc/yum.repos.d/plasma-unstable.repo && \
    dnf -y up && dnf -y in --setopt=install_weak_deps=False \
            binutils \
            bsdtar \
            copr-cli \
            createrepo_c \
            distribution-gpg-keys \
            file \
            fuse-overlayfs \
            git-core \
            gnupg2 \
            jq \
            kf6-srpm-macros \
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
