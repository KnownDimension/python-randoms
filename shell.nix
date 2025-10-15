let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pandas 
      python-pkgs.requests
      python-pkgs.pygobject3
    ]))

    pkgs.gobject-introspection
    pkgs.gtk4
    pkgs.gtk4.dev
    pkgs.gtk4.out
    pkgs.graphene
    pkgs.graphene.dev

  ];

  shellHook = ''
    export GI_TYPELIB_PATH="${pkgs.gtk4}/lib/girepository-1.0":${pkgs.graphene}/lib/girepository-1.0"

  '';



}

# all stolen shamelessly from the nixos wiki, pandas may be needed at somepoint