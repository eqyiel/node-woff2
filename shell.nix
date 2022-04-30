{ nodeVersion ? "nodejs-12_x" }:

let
  # nix-prefetch-url --unpack https://github.com/NixOS/nixpkgs/archive/6766fb6503ae1ebebc2a9704c162b2aef351f921.tar.gz
  nixpkgs =
    import
      (builtins.fetchTarball {
        name = "nixpkgs-unstable-2022-04-30";
        url = https://github.com/NixOS/nixpkgs/archive/6766fb6503ae1ebebc2a9704c162b2aef351f921.tar.gz;
        sha256 = "1a805n9iqlbmffkzq3l6yf2xp74wjaz5pdcp0cfl0rhc179w4lpy";
      })
      { };

  nodejs = builtins.getAttr nodeVersion nixpkgs.pkgs;
in
nixpkgs.pkgs.mkShell {
  packages = [
    nodejs
    nixpkgs.pkgs.python3
  ] ++ (with nixpkgs.pkgs.nodePackages; [
    (nixpkgs.pkgs.yarn.override { nodejs = nodejs; })
  ]);

  shellHook = ''
    # Teach node-gyp where to find headers locally
    export npm_config_nodedir=${nodejs}
  '';
}
