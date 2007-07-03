%define eclipse_base	%{_datadir}/eclipse
%define gcj_support     1

Name:		eclipse-sdk-nls
Version:	3.2.1
Release:	%mkrel 3.2
Summary:	Eclipse language packs for the Eclipse SDK
Group:		Development/Java
License:	Eclipse Public License
URL:		http://eclipse.org

Source0:	http://download.eclipse.org/eclipse/downloads/drops/L-3.2.1_Language_Packs-200609210945/NLpack1-eclipse-SDK-3.2.1-gtk.zip
Source1:	http://download.eclipse.org/eclipse/downloads/drops/L-3.2.1_Language_Packs-200609210945/NLpack2-eclipse-SDK-3.2.1-gtk.zip
Source2:	http://download.eclipse.org/eclipse/downloads/drops/L-3.2.1_Language_Packs-200609210945/NLpack2a-eclipse-SDK-3.2.1-gtk.zip
Source3:	http://download.eclipse.org/eclipse/downloads/drops/L-3.2.1_Language_Packs-200609210945/NLpackBidi-eclipse-SDK-3.2.1-gtk.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	eclipse-nlspackager
BuildRequires:	dos2unix

Requires:	eclipse-rcp

%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
BuildRequires:  java-devel
%endif

%package cs
Summary:		Eclipse SDK language pack for Czech
Group:			Development/Java
Requires:		eclipse-rcp

%package hu
Summary:		Eclipse SDK language pack for Hungarian
Group:			Development/Java
Requires:		eclipse-rcp

%package pl
Summary:		Eclipse SDK language pack for Polish
Group:			Development/Java
Requires:		eclipse-rcp

%package ru
Summary:		Eclipse SDK language pack for Russian
Group:			Development/Java
Requires:		eclipse-rcp

%package ar
Summary:		Eclipse SDK language pack for Arabic
Group:			Development/Java
Requires:		eclipse-rcp

%package iw
Summary:		Eclipse SDK language pack for Hebrew
Group:			Development/Java
Requires:		eclipse-rcp

%package da
Summary:		Eclipse SDK language pack for Danish
Group:			Development/Java
Requires:		eclipse-rcp

%package de
Summary:		Eclipse SDK language pack for German
Group:			Development/Java
Requires:		eclipse-rcp

%package el
Summary:		Eclipse SDK language pack for Greek
Group:			Development/Java
Requires:		eclipse-rcp

%package es
Summary:		Eclipse SDK language pack for Spanish
Group:			Development/Java
Requires:		eclipse-rcp

%package fi
Summary:		Eclipse SDK language pack for Finnish
Group:			Development/Java
Requires:		eclipse-rcp

%package fr
Summary:		Eclipse SDK language pack for French
Group:			Development/Java
Requires:		eclipse-rcp

%package it
Summary:		Eclipse SDK language pack for Italian
Group:			Development/Java
Requires:		eclipse-rcp

%package ja
Summary:		Eclipse SDK language pack for Japanese
Group:			Development/Java
Requires:		eclipse-rcp

%package ko
Summary:		Eclipse SDK language pack for Korean
Group:			Development/Java
Requires:		eclipse-rcp

%package nl
Summary:		Eclipse SDK language pack for Dutch
Group:			Development/Java
Requires:		eclipse-rcp

%package no
Summary:		Eclipse SDK language pack for Norwegian
Group:			Development/Java
Requires:		eclipse-rcp

%package pt		
Summary:		Eclipse SDK language pack for Portuguese
Group:			Development/Java
Requires:		eclipse-rcp

%package sv		
Summary:		Eclipse SDK language pack for Swedish
Group:			Development/Java
Requires:		eclipse-rcp

%package tr		
Summary:		Eclipse SDK language pack for Turkish
Group:			Development/Java
Requires:		eclipse-rcp

%package zh		
Summary:		Eclipse SDK language pack for Chinese
Group:			Development/Java
Requires:		eclipse-rcp

%description
This package contains multiple language translations for the Eclipse SDK.

	
%description cs
Eclipse language pack for Czech translations.

%description hu
Eclipse language pack for Hungarian translations.

%description pl
Eclipse language pack for Polish translations.

%description ru
Eclipse language pack for Russian translations.

%description ar
Eclipse language pack for Arabic translations.

%description iw
Eclipse language pack for Hebrew translations.

%description de
Eclipse language pack for German translations.

%description es
Eclipse language pack for Spanish translations.

%description fr
Eclipse language pack for French translations.

%description it
Eclipse language pack for Italian translations.

%description ko
Eclipse language pack for Korean translations.

%description ja
Eclipse language pack for Japanese translations.

%description pt
Eclipse language pack for Portuguese (and Brazilian Portuguese) translations.

%description zh
Eclipse language pack for Chinese (Simplified and Traditional) translations.

%description da
Eclipse language pack for Danish translations.

%description nl
Eclipse language pack for Dutch translations.

%description fi
Eclipse language pack for Finnish translations.

%description el
Eclipse language pack for Greek translations.

%description no
Eclipse language pack for Norwegian translations.

%description sv
Eclipse language pack for Swedish translations.

%description tr
Eclipse language pack for Turkish translations.

%prep
%setup -q -c -n sdk-langpack


%build
cp -r %{eclipse_base} SDK
SDK=$(cd SDK > /dev/null && pwd)

# Eclipse may try to write to the home directory.
mkdir home
homedir=$(cd home > /dev/null && pwd)

mkdir langpacks
# Run the langpackager application  
%{java}	\
	-cp $SDK/startup.jar			\
	-Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration \
	-Duser.home=$homedir			\
	org.eclipse.core.launcher.Main		\
	-consolelog				\
	-application org.eclipse.linuxtools.nlspackager.NLSPackagerApplication \
	-d langpacks %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} 


%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{eclipse_base}/plugins \
		$RPM_BUILD_ROOT%{eclipse_base}/features

cp -p -r langpacks/eclipse $RPM_BUILD_ROOT%{eclipse_base}/..


# Find all corresponding feature/plugin files and list then in a file
# to tag them as files.
 
find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.cs_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > cs.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.cs_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> cs.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.hu_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > hu.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.hu_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> hu.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.pl_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > pl.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.pl_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> pl.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.ru_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > ru.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.ru_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> ru.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.ar_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > ar.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.ar_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> ar.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.iw_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > iw.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.iw_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> iw.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.de_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > de.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.de_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> de.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.da_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > da.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.da_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> da.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.el_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > el.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.el_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> el.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.es_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > es.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.es_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> es.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.fi_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > fi.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.fi_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> fi.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.fr_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > fr.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.fr_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> fr.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.it_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > it.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.it_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> it.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.ja_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > ja.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.ja_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> ja.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.ko_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > ko.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.ko_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> ko.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.nl_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > nl.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.nl_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> nl.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.no_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > no.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.no_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> no.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.pt_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > pt.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.pt_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> pt.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.sv_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > sv.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.sv_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> sv.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.tr_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > tr.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.tr_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> tr.files

find $RPM_BUILD_ROOT%{eclipse_base}/features -regex \.*.zh_\.*[^0-9]$ \
	| sed -e s:$RPM_BUILD_ROOT:: > zh.files
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.zh_*	\
	| sed -e s:$RPM_BUILD_ROOT:: >> zh.files

# Mark each license file 'epl-v10.html' in features with with doc tag

sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" cs.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" hu.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" pl.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" ru.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" ar.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" iw.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" de.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" da.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" el.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" es.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" fi.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" fr.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" it.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" ja.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" ko.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" nl.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" no.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" pt.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" sv.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" tr.files
sed -i "s:\(.*\)\(epl-v10.html\):%doc\ \1\2:" zh.files

# Use dos2unix on all epl-v10.html files since it seems to be created
# on a non-Unix system.

find $RPM_BUILD_ROOT%{eclipse_base} -regex \.*epl-v10.html -exec dos2unix '{}' \;

# A bug creates a plugin that should not exist. So delete these here for now,
# but needs to be fixed in eclipse-nlspackager.

find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.cu_* -delete
find $RPM_BUILD_ROOT%{eclipse_base}/plugins -name *.ac_* -delete


find $RPM_BUILD_ROOT%{eclipse_base}/features -maxdepth 1 -type d \
	-name *.ac_* -exec rm -rf '{}' \; 

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post cs
%{update_gcjdb}

%postun cs
%{clean_gcjdb}

%post hu
%{update_gcjdb}

%postun hu
%{clean_gcjdb}

%post pl
%{update_gcjdb}

%postun pl
%{clean_gcjdb}

%post ru
%{update_gcjdb}

%postun ru
%{clean_gcjdb}

%post ar
%{update_gcjdb}

%postun ar
%{clean_gcjdb}

%post iw
%{update_gcjdb}

%postun iw
%{clean_gcjdb}

%post da
%{update_gcjdb}

%postun da
%{clean_gcjdb}

%post de
%{update_gcjdb}

%postun de
%{clean_gcjdb}

%post el
%{update_gcjdb}

%postun el
%{clean_gcjdb}

%post es
%{update_gcjdb}

%postun es
%{clean_gcjdb}

%post fi
%{update_gcjdb}

%postun fi
%{clean_gcjdb}

%post fr
%{update_gcjdb}

%postun fr
%{clean_gcjdb}

%post it
%{update_gcjdb}

%postun it
%{clean_gcjdb}

%post ja
%{update_gcjdb}

%postun ja
%{clean_gcjdb}

%post ko
%{update_gcjdb}

%postun ko
%{clean_gcjdb}

%post nl
%{update_gcjdb}

%postun nl
%{clean_gcjdb}

%post no
%{update_gcjdb}

%postun no
%{clean_gcjdb}

%post pt
%{update_gcjdb}

%postun pt
%{clean_gcjdb}

%post sv
%{update_gcjdb}

%postun sv
%{clean_gcjdb}

%post tr
%{update_gcjdb}

%postun tr
%{clean_gcjdb}

%post zh
%{update_gcjdb}

%postun zh
%{clean_gcjdb}
%endif

%files cs -f cs.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.cs_*
%endif

%files hu -f hu.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.hu_*
%endif

%files pl -f pl.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.pl_*
%endif

%files ru -f ru.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.ru_*
%endif

%files ar -f ar.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.ar_*
%endif

%files iw -f iw.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.iw_*
%endif

%files da -f da.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.da_*
%endif

%files de -f de.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.de_*
%endif

%files el -f el.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.el_*
%endif

%files es -f es.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.es_*
%endif

%files fi -f fi.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.fi_*
%endif

%files fr -f fr.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.fr_*
%endif

%files it -f it.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.it_*
%endif

%files ja -f ja.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.ja_*
%endif

%files ko -f ko.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.ko_*
%endif

%files nl -f nl.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.nl_*
%endif

%files no -f no.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.no_*
%endif

%files pt -f pt.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.pt_*
%endif

%files sv -f sv.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.sv_*
%endif

%files tr -f tr.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.tr_*
%endif

%files zh -f zh.files
%defattr(0644,root,root,0755)
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*.zh_*
%endif
