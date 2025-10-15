let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pandas 
      python-pkgs.requests
      python-pkgs.pygobject3
    ]))
  ];
}

# all stolen shamelessly from the nixos wiki, pandas may be needed at somepoint