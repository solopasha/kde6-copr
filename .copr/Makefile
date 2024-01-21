.PHONY: prepare goprep srpm
specfile = $(notdir $(spec))

prepare:
	dnf install --nodocs --setopt=install_weak_deps=0 \
				--repofrompath 'kde6,https://download.copr.fedorainfracloud.org/results/solopasha/kde6/fedora-39-x86_64/devel' \
				--setopt='kde6.gpgkey=https://download.copr.fedorainfracloud.org/results/solopasha/kde6/pubkey.gpg' kf6-srpm-macros
	dnf install --nodocs --setopt=install_weak_deps=0 rpmdevtools

goprep:
	dnf install --nodocs -y golang git-core
	go env -w GOPROXY=https://proxy.golang.org,direct
	go env -w GOSUMDB=sum.golang.org
	bash bundle_go_deps_for_rpm.sh $(specfile)

%spec:
	@:

ollama.spec: goprep

srpm: prepare $(specfile)
	spectool -g ./$(specfile)
	rpmbuild -bs --define "_sourcedir ${PWD}" --define "_specdir ${PWD}" \
		--define "_builddir ${PWD}" --define "_srcrpmdir $(outdir)" --define \
		"_rpmdir ${PWD}" --define "_buildrootdir ${PWD}/.build" $(specfile)
