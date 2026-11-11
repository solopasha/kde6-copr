# solopasha's repositories with KDE packages

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

## GitHub repositories and snapshots

Packages are also published to a GitHub [repository](https://solopasha.github.io/kde6-copr/) (built with GitHub Actions). This repository serves as a mirror and backup in case COPR is slow or unavailable. In the future, the COPR repositories may be discontinued, and the GitHub repositories may become the primary package source.

[Snapshot repositories](https://solopasha.github.io/kde6-copr/snapshots/) provide dated package builds, allowing users to access packages from a specific point in time. This can be useful for rolling back to an earlier version.
