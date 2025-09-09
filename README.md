# Solopasha's repositories with KDE packages

Plasma and Frameworks from git - [solopasha/plasma-unstable](https://copr.fedorainfracloud.org/coprs/solopasha/plasma-unstable/)

Gear (KDE Applications) from git - [solopasha/kde-gear-unstable](https://copr.fedorainfracloud.org/coprs/solopasha/kde-gear-unstable)

## Installation instructions

Plasma+Frameworks+Gear:

```bash
sudo dnf copr enable solopasha/kde-gear-unstable -y && \
sudo dnf offline-upgrade download && \
sudo dnf offline-upgrade reboot
```

Plasma and Frameworks only:

```bash
sudo dnf copr enable solopasha/plasma-unstable -y && \
sudo dnf offline-upgrade download && \
sudo dnf offline-upgrade reboot
```

Although Copr is rarely slow or unstable when building packages, Plasma and Frameworks packages are also published to a GitHub repository (built with GitHub Actions). This is a mirror/backup repository:

```bash
sudo dnf config-manager addrepo --from-repofile=https://solopasha.github.io/kde6-copr/unstable/kde6-copr-unstable.repo
```

Atomic image:

```bash
sudo rpm-ostree rebase ostree-unverified-registry:ghcr.io/solopasha/kde6-copr/kde-unstable:latest
```
