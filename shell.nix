# This file is created for nix-shell users who want an environment with necessary python packages installed
# Just kidding, I couldn't install numpy globally in my nix system so I had to create a shell.nix file
# Cool stuff though

let pkgs = import <nixpkgs> { };
in pkgs.mkShell {
  packages = with pkgs;
    [
      python3.pkgs.numpy
      # (pkgs.python3.withPackages (python-pkgs: [
      #   # select Python packages here
      #   python-pkgs.pandas
      #   python-pkgs.requests
      #   python-pkgs.numpy
      # ]))
    ];
}
