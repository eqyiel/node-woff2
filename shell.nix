{ nixpkgs ? <nixpkgs>, system ? builtins.currentSystem }:

let

  nixpkgsLocal = import nixpkgs { inherit system; };

  nixpkgsUnstable = with nixpkgsLocal.pkgs; callPackage (stdenv.mkDerivation rec {
    name = "nixpkgs-unstable-${version}";
    version = "2018-08-10";

    src = fetchFromGitHub {
      owner = "NixOS";
      repo = "nixpkgs-channels";
      rev = "bf1b50cbc8ffe9747758d089e3148406a7ce5c21";
      sha256 = "0clczc8n7415i7pcqs1my8ydf0sijkcwqw6c36dgn998kdrgknh8";
    };

    dontBuild = true;
    preferLocalBuild = true;

    installPhase = ''
      cp -a . $out
    '';
  }) { inherit system; };

in with nixpkgsUnstable.pkgs; stdenv.mkDerivation rec {
  name = "node-woff2-env";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = with pkgs; [
    nodejs-6_x
    python
  ] ++ (with nodePackages_6_x; [
    yarn node-gyp
  ]);
  shellHook = ''
    echo ✨ environment ready!
  '';
}
