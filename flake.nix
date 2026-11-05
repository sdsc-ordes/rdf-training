{
  description = "RDF / knowledge graph course: slides, hands-on and checks";

  inputs.nixpkgs.url = "https://channels.nixos.org/nixos-unstable/nixexprs.tar.xz";

  outputs = { nixpkgs, ... }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      forAll = f: nixpkgs.lib.genAttrs systems (s: f nixpkgs.legacyPackages.${s});
    in {
      devShells = forAll (pkgs: {
        default = pkgs.mkShell {
          packages = [ pkgs.nodejs_24 pkgs.uv pkgs.python313 pkgs.git pkgs.just ]
            ++ pkgs.lib.optional pkgs.stdenv.hostPlatform.isLinux pkgs.chromium;
          shellHook = ''
            export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
            export UV_PYTHON=${pkgs.python313}/bin/python3 UV_PYTHON_DOWNLOADS=never
          '' + pkgs.lib.optionalString pkgs.stdenv.hostPlatform.isLinux ''
            export SLIDEV_CHROMIUM=${pkgs.chromium}/bin/chromium
            # prebuilt wheels (e.g. pyoxigraph) need libstdc++
            export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib ]}''${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
          '';
        };
      });
    };
}
