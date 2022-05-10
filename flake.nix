{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    utils.url = "github:gytis-ivaskevicius/flake-utils-plus";
  };

  outputs = { self, nixpkgs, utils } @ inputs:
    utils.lib.mkFlake {
      inherit self inputs;

      outputsBuilder = channels:
        let pkgs = channels.nixpkgs; in
        with pkgs;
        rec {
          devShells = rec {
            default = pearson-pdf;
            pearson-pdf = (poetry2nix.mkPoetryEnv { projectDir = ./.; }).env;
          };

          packages = (self.overlays.default pkgs pkgs) // {
            default = packages.pearson-pdf;
          };
        };

      overlays = rec {
        default = pearson-pdf;
        pearson-pdf = final: prev: {
          pearson-pdf = final.poetry2nix.mkPoetryApplication { projectDir = ./.; };
        };
      };
    };
}
