.PHONY: prepare srpm goprep
specfile = $(notdir $(spec))

prepare:
	dnf install --nodocs -y --setopt=install_weak_deps=0 --repo=kde6-beta \
				--repofrompath 'kde6-beta,https://download.copr.fedorainfracloud.org/results/solopasha/kde6-beta/fedora-42-x86_64/devel/' \
				--setopt='kde6-beta.gpgcheck=1' \
				--setopt='kde6-beta.gpgkey=https://download.copr.fedorainfracloud.org/results/solopasha/kde6-beta/pubkey.gpg' \
				kf6-srpm-macros

goprep:
	dnf install --nodocs -y golang git-core go-vendor-tools rpmdevtools python3-specfile
	spectool -g ./$(specfile)
	go_vendor_archive create --config ./go-vendor-tools.toml ./$(specfile)

%spec: FORCE
	@:

FORCE: ;

gocryptfs.spec: goprep

srpm: prepare $(specfile)
	rpmbuild -bs --define "_sourcedir ${PWD}" --define "_specdir ${PWD}" \
		--define "_builddir ${PWD}" --define "_srcrpmdir $(outdir)" --define \
		"_rpmdir ${PWD}" --define "_disable_source_fetch 0" $(specfile)
