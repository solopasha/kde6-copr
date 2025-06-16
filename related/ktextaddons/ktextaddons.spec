Name:           ktextaddons
Version:        1.6.0
Release:        2%{?dist}
Summary:        Various text handling addons

License:        CC0-1.0 AND LGPL-2.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://invent.kde.org/libraries/ktextaddons
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        https://invent.kde.org/sysadmin/release-keyring/-/raw/master/keys/mlaurent@key1.asc?ref_type=heads#/signing-key.pgp
BuildSystem:    cmake_kf6

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(Qt6Keychain)

%description
%{summary}.

%package        qt6
Summary:        Qt6 libraries for %{name}
Requires:       %{name}-common = %{version}-%{release}
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}
%description    qt6-devel
%{summary}.

%package        common
Summary:        Translations and documents for %{name}
Obsoletes:      ktextaddons-docs < 1.5.3-1
BuildArch:      noarch
%description    common
%{summary}.

%prep -p
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%files qt6
%license LICENSES/
%{_kf6_datadir}/qlogging-categories6/ktextaddons.categories
%{_kf6_datadir}/qlogging-categories6/ktextaddons.renamecategories
%{_kf6_libdir}/libKF6TextAddonsWidgets.so.%{version}
%{_kf6_libdir}/libKF6TextAddonsWidgets.so.1
%{_kf6_libdir}/libKF6TextAutoCorrectionCore.so.%{version}
%{_kf6_libdir}/libKF6TextAutoCorrectionCore.so.1
%{_kf6_libdir}/libKF6TextAutoCorrectionWidgets.so.%{version}
%{_kf6_libdir}/libKF6TextAutoCorrectionWidgets.so.1
%{_kf6_libdir}/libKF6TextAutoGenerateText.so
%{_kf6_libdir}/libKF6TextAutoGenerateText.so.%{version}
%{_kf6_libdir}/libKF6TextAutoGenerateText.so.1
%{_kf6_libdir}/libKF6TextCustomEditor.so.%{version}
%{_kf6_libdir}/libKF6TextCustomEditor.so.1
%{_kf6_libdir}/libKF6TextEditTextToSpeech.so.%{version}
%{_kf6_libdir}/libKF6TextEditTextToSpeech.so.1
%{_kf6_libdir}/libKF6TextEmoticonsCore.so.%{version}
%{_kf6_libdir}/libKF6TextEmoticonsCore.so.1
%{_kf6_libdir}/libKF6TextEmoticonsWidgets.so.%{version}
%{_kf6_libdir}/libKF6TextEmoticonsWidgets.so.1
%{_kf6_libdir}/libKF6TextGrammarCheck.so.%{version}
%{_kf6_libdir}/libKF6TextGrammarCheck.so.1
%{_kf6_libdir}/libKF6TextSpeechToText.so
%{_kf6_libdir}/libKF6TextSpeechToText.so.%{version}
%{_kf6_libdir}/libKF6TextSpeechToText.so.1
%{_kf6_libdir}/libKF6TextTranslator.so.%{version}
%{_kf6_libdir}/libKF6TextTranslator.so.1
%{_kf6_libdir}/libKF6TextUtils.so.%{version}
%{_kf6_libdir}/libKF6TextUtils.so.1
%{_kf6_libdir}/libtextautogenerateollama.so.%{version}
%{_kf6_libdir}/libtextautogenerateollama.so.1
%{_kf6_plugindir}/speechtotext/
%{_kf6_plugindir}/textautogeneratetext/
%{_kf6_plugindir}/translator/

%files qt6-devel
%{_kf6_includedir}/TextAddonsWidgets/
%{_kf6_includedir}/TextAutoCorrectionCore/
%{_kf6_includedir}/TextAutoCorrectionWidgets/
%{_kf6_includedir}/TextAutoGenerateText/
%{_kf6_includedir}/TextCustomEditor/
%{_kf6_includedir}/TextEditTextToSpeech/
%{_kf6_includedir}/TextEmoticonsCore/
%{_kf6_includedir}/TextEmoticonsWidgets/
%{_kf6_includedir}/TextGrammarCheck/
%{_kf6_includedir}/TextSpeechToText/
%{_kf6_includedir}/TextTranslator/
%{_kf6_includedir}/TextUtils/
%{_kf6_libdir}/cmake/KF6TextAddonsWidgets/
%{_kf6_libdir}/cmake/KF6TextAutoCorrectionCore/
%{_kf6_libdir}/cmake/KF6TextAutoCorrectionWidgets/
%{_kf6_libdir}/cmake/KF6TextAutoGenerateText/
%{_kf6_libdir}/cmake/KF6TextCustomEditor/
%{_kf6_libdir}/cmake/KF6TextEditTextToSpeech/
%{_kf6_libdir}/cmake/KF6TextEmoticonsCore/
%{_kf6_libdir}/cmake/KF6TextEmoticonsWidgets/
%{_kf6_libdir}/cmake/KF6TextGrammarCheck/
%{_kf6_libdir}/cmake/KF6TextSpeechToText/
%{_kf6_libdir}/cmake/KF6TextTranslator/
%{_kf6_libdir}/cmake/KF6TextUtils/
%{_kf6_libdir}/libKF6TextAddonsWidgets.so
%{_kf6_libdir}/libKF6TextAutoCorrectionCore.so
%{_kf6_libdir}/libKF6TextAutoCorrectionWidgets.so
%{_kf6_libdir}/libKF6TextAutoGenerateText.so
%{_kf6_libdir}/libKF6TextCustomEditor.so
%{_kf6_libdir}/libKF6TextEditTextToSpeech.so
%{_kf6_libdir}/libKF6TextEmoticonsCore.so
%{_kf6_libdir}/libKF6TextEmoticonsWidgets.so
%{_kf6_libdir}/libKF6TextGrammarCheck.so
%{_kf6_libdir}/libKF6TextSpeechToText.so
%{_kf6_libdir}/libKF6TextTranslator.so
%{_kf6_libdir}/libKF6TextUtils.so
%{_kf6_qtplugindir}/designer/textcustomeditor.so
%{_kf6_qtplugindir}/designer/texttranslatorwidgets6.so

%files common -f %{name}.lang
%doc README.md

%changelog
* Mon Jun 16 2025 Pavel Solovev <daron439@gmail.com> - 1.6.0-2
- rebuilt

* Mon Jun 02 2025 Pavel Solovev <daron439@gmail.com> - 1.6.0-1
- new version

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Marie Loise Nolden <loise@kde.org> - 1.5.4-1
- update to 1.5.4

* Sun Mar 10 2024 Marie Loise Nolden <loise@kde.org> - 1.5.3-5
- add missing BuildArch: noarch to -qt6-doc package

* Sun Mar 3 2024 Marie Loise Nolden <loise@kde.org> - 1.5.3-4
- move qt designer plugin to -devel (qt5 and qt6)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Alessandro Astone <ales.astone@gmail.com> - 1.5.3-1
- 1.5.3
- Rename "docs" subpackage to "common", as it doesn't make sense to have string translations in "docs"
- Add qt6-doc subpackage for KF6 API

* Tue Dec 5 2023 Steve Cossette <farchord@gmail.com> - 1.5.2-1
- 1.5.2

* Sun Sep 24 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 08 2023 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1.1-2
- Add missing BuildRequires: cmake(Qt5TextToSpeech)

* Fri Mar 24 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.1-1
- Update to version 1.1.1

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-5
- Use proper license field

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-4
- Add license and doc files

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-3
- Add BuildRequires: cmake

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-2
- Move header files to the devel subpackage

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-1
- Initial release
