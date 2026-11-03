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
          packages = [ pkgs.nodejs_24 pkgs.uv pkgs.git ]
            ++ pkgs.lib.optional pkgs.stdenv.hostPlatform.isLinux pkgs.chromium;
          shellHook = ''
            export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
          '' + pkgs.lib.optionalString pkgs.stdenv.hostPlatform.isLinux ''
            export SLIDEV_CHROMIUM=${pkgs.chromium}/bin/chromium
          '';
        };
      });
    };
}
