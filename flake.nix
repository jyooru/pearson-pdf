{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, flake-utils, nixpkgs }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; }; in
      with pkgs; rec {
        devShell = packages.env.env;
        packages.env = poetry2nix.mkPoetryEnv { projectDir = ./.; };
      }
    );
}
