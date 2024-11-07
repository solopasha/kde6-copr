.PHONY: prepare goprep srpm
specfile = $(notdir $(spec))

prepare:
	dnf install --nodocs --setopt=install_weak_deps=0 --disablerepo=\* \
				--repofrompath 'kde6,https://download.copr.fedorainfracloud.org/results/solopasha/kde6/fedora-40-x86_64/' \
				--setopt='kde6.gpgkey=https://download.copr.fedorainfracloud.org/results/solopasha/kde6/pubkey.gpg' \
				kf6-srpm-macros

goprep:
	dnf install --nodocs -y --repofrompath 'golang-rawhide,https://download.copr.fedorainfracloud.org/results/@go-sig/golang-rawhide/fedora-$$releasever-$$basearch/' \
                --setopt='golang-rawhide.gpgkey=https://download.copr.fedorainfracloud.org/results/@go-sig/golang-rawhide/pubkey.gpg' \
				golang git-core go-vendor-tools askalono-cli rpmdevtools
	spectool -g ./$(specfile)
	go_vendor_archive create --config go-vendor-tools.toml $(specfile)

%spec:
	@:

ollama.spec: goprep

srpm: prepare $(specfile)
	rpmbuild -bs --define "_sourcedir ${PWD}" --define "_specdir ${PWD}" \
		--define "_builddir ${PWD}" --define "_srcrpmdir $(outdir)" --define \
		"_rpmdir ${PWD}" --define "_disable_source_fetch 0" $(specfile)
