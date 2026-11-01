ARG VERSION=45

FROM ghcr.io/oras-project/oras:v1.3.6 AS oras

ARG OCI_REF=ghcr.io/solopashachas/testrpm/kf6:latest-unstable-44

RUN mkdir /out && \
    oras pull "${OCI_REF}" -o /out


FROM registry.fedoraproject.org/fedora:$VERSION

COPY --from=oras /out /tmp/rpms

RUN rm /usr/share/dnf5/repos.d/fedora-cisco-openh264.repo && \
    dnf -y in /tmp/rpms/kf6-resultdir/kf6-srpm-macros*.rpm && \
    dnf -y up && dnf -y in --nodocs --setopt=install_weak_deps=False \
    'dnf5-command(repoclosure)' \
    binutils \
    bsdtar \
    # copr-cli \
    createrepo_c \
    curl \
    distribution-gpg-keys \
    fd-find \
    file \
    gh \
    git-core \
    gnupg2 \
    jq \
    libabigail \
    luajit \
    parallel \
    perl-interpreter \
    python3-pyelftools \
    rpm-sign \
    rpmdevtools \
    tar \
    yq \
    zstd && \
    dnf -y upgrade --enablerepo=updates-testing --refresh --advisory=FEDORA-2026-8c0b575c3c && \
    dnf clean all && \
    useradd -M -u 1001 builduser

USER builduser
