# Generated by go2rpm
%bcond_without check

# https://github.com/rs/cors
%global goipath         github.com/rs/cors
Version:                1.6.0

%gometa

%global common_description %{expand:
CORS is a net/http handler implementing Cross Origin Resource Sharing W3
specification in Golang.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go net/http configurable handler to handle CORS requests

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/codegangsta/negroni)
BuildRequires:  golang(github.com/gin-gonic/gin)
BuildRequires:  golang(github.com/go-martini/martini)
# Only in examples and with lots of cyclic deps
# BuildRequires:  golang(github.com/gobuffalo/buffalo)
# BuildRequires:  golang(github.com/gobuffalo/buffalo/render)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/julienschmidt/httprouter)
BuildRequires:  golang(github.com/justinas/alice)
BuildRequires:  golang(github.com/martini-contrib/render)
BuildRequires:  golang(github.com/pressly/chi)
BuildRequires:  golang(github.com/zenazn/goji)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 15:05:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.0-1
- Initial package
