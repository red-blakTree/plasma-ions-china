%global project plasma-ions-china
%global ion_headers_version 6.6.4

Name:           %{project}
Version:        %{ion_headers_version}
Release:        1%{?dist}
Summary:        KDE Plasma weather ions for Chinese users

# GPL-3.0-or-later: see LICENSE.txt (GNU GPL v3, 29 June 2007).
License:        GPL-3.0-or-later
URL:            https://github.com/red-blakTree/plasma-ions-china
Source0:        %{url}/archive/v%{version}/%{project}-v%{version}.tar.gz

# Runtime libraries: the ion is a plugin loaded by the Plasma weather widget,
# and it links against the weather engine shipped in kdeplasma-addons.
Requires:       kdeplasma-addons

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  qt6-qtbase-devel
# Requested by kdeplasma-addons, which is configured in-tree to obtain ion.h.
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquick3d-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kunitconversion-devel
BuildRequires:  libplasma-devel
BuildRequires:  kf6-kauth-devel
BuildRequires:  kf6-kcmutils-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kdeclarative-devel
BuildRequires:  kf6-kglobalaccel-devel
BuildRequires:  kf6-kholidays-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  kf6-kitemmodels-devel
BuildRequires:  kf6-kjobwidgets-devel
BuildRequires:  kf6-knewstuff-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kpackage-devel
BuildRequires:  kf6-krunner-devel
BuildRequires:  kf6-kservice-devel
BuildRequires:  kf6-ksvg-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-purpose-devel
BuildRequires:  kf6-sonnet-devel

%description
A collection of KDE Plasma weather ions for Chinese users.

This package provides the modern (KDE >= 6.5) ion plugin nmccn, which fetches
weather data from the National Meteorological Center of China.

%prep
# The archive may come from git archive or from a plain `tar` of the checkout
# plus --transform; both put every file under ./%{project}-v%{version}/, so the
# default -p1 strip of %setup lands on the expected directory.
%autosetup -n %{project}-v%{version}

%build
# PLASMA_IONS_CHINA_VERSION is passed explicitly because the top-level
# CMakeLists.txt aborts on `git describe` output that is not a vX.Y.Z tag, and
# release tarballs carry no git information at all.
%cmake \
    -DPLASMA_IONS_CHINA_VERSION=%{version} \
    -DPLASMA_IONS_CHINA_ENABLE_MODERN=ON \
    -DPLASMA_IONS_CHINA_ENABLE_LEGACY=OFF

%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_datadir}/plasma/weather_ions/
%{_libdir}/plugins/plasma/weather/n*ccn.so
