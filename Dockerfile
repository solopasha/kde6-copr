
ARG VERSION=42

FROM registry.fedoraproject.org/fedora-minimal:$VERSION

COPY <<'EOF' /etc/yum.repos.d/coprs.repo
[copr:copr.fedorainfracloud.org:solopasha:plasma-unstable]
name=Copr repo for plasma-unstable owned by solopasha
baseurl=https://download.copr.fedorainfracloud.org/results/solopasha/plasma-unstable/fedora-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/solopasha/plasma-unstable/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1
priority=97

[copr:copr.fedorainfracloud.org:solopasha:playground]
name=Copr repo for playground owned by solopasha
baseurl=https://download.copr.fedorainfracloud.org/results/solopasha/playground/fedora-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/solopasha/playground/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1
priority=97
EOF

RUN rm /etc/yum.repos.d/fedora-cisco-openh264.repo && \
    dnf -y up && dnf -y in --nodocs --setopt=install_weak_deps=False \
            binutils \
            bsdtar \
            copr-cli \
            createrepo_c \
            curl \
            distribution-gpg-keys \
            fd-find \
            file \
            fuse-overlayfs \
            gh \
            git-core \
            gnupg2 \
            jq \
            kf6-srpm-macros \
            libabigail \
            luajit \
            mock \
            nosync \
            parallel \
            perl-interpreter \
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
