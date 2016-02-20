with import <nixpkgs> {}; {
  pySoccerEnv = stdenv.mkDerivation {
    name = "soccer";
    buildInputs = [ stdenv pythonFull pythonPackages.virtualenv pythonPackages.ipython ];
    shellHook =
      ''
        if [ ! -d venv ]
        then
          virtualenv venv
          venv/bin/pip install -r requirements.txt
        fi
        source venv/bin/activate
      '';
  };
}
