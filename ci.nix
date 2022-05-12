with builtins;

let
  flake = getFlake (toString ./.);
in

with flake.inputs.nixpkgs.lib;

{
  packages = recurseIntoAttrs flake.packages.${currentSystem};
}
