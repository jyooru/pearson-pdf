with builtins;

let
  flake = getFlake (toString ./.);
in

with flake.inputs.nixpkgs.lib;

{
  devShells = recurseIntoAttrs flake.devShells.${currentSystem};
  packages = recurseIntoAttrs flake.packages.${currentSystem};
}
