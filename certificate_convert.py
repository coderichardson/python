import subprocess
import sys


def run_openssl(command):
    """Run an OpenSSL command and stream output to the console."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print("An error occurred while running OpenSSL.")
        sys.exit(1)


def pem_to_pfx():
    selected_cert = input(
        "Enter the name of the PEM certificate to convert to PFX (include .pem): "
    )
    selected_key = input(
        "Enter the name of the private key associated with the PEM certificate (include .key/.pem): "
    )
    converted_name = input(
        "Enter the name of the desired PFX file (include .pfx): "
    )

    command = [
        "openssl", "pkcs12",
        "-inkey", selected_key,
        "-in", selected_cert,
        "-export",
        "-out", converted_name
    ]

    run_openssl(command)


def pfx_to_pem():
    selected_cert = input(
        "Enter the name of the PFX certificate to convert to PEM (include .pfx): "
    )
    converted_name = input(
        "Enter the name of the desired PEM file (include .pem): "
    )

    command = [
        "openssl", "pkcs12",
        "-in", selected_cert,
        "-out", converted_name,
        "-nodes"
    ]

    run_openssl(command)


def generate_csr():
    selected_key = input(
        "Enter the name of the private key to use (include .pem), or press Enter to generate one: "
    ).strip()

    selected_csr = input(
        "Enter the name of the CSR (include .csr): "
    ).strip()

    # If no private key name was provided, generate one
    if not selected_key:
        selected_key = "private_key.pem"
        print(f"No private key provided. Generating new private key: {selected_key}")

        run_openssl([
            "openssl", "genpkey",
            "-algorithm", "RSA",
            "-pkeyopt", "rsa_keygen_bits:2048",
            "-out", selected_key
        ])
    else:
        print(f"Using existing private key: {selected_key}")

    # Generate CSR using the selected or newly created private key
    run_openssl([
        "openssl", "req",
        "-new",
        "-key", selected_key,
        "-out", selected_csr
    ])

    print(f"CSR successfully created: {selected_csr}")


def generate_pem():
    selected_key = input(
        "Enter the name of the private key to correspond with the CSR (include .pem): "
    )
    selected_csr = input(
        "Enter the name of the CSR (include .csr): "
    )
    output_cert = input(
        "Enter the name of the output PEM certificate (include .pem): "
    )

    run_openssl([
    "openssl", "x509",
    "-req",
    "-in", selected_csr,
    "-signkey", selected_key,
    "-out", output_cert,
    "-days", "365"
    ])


def main():
    choice = input(
        "Choose one of the following (1–4):\n\n"
        "1. Convert a PEM certificate to PFX.\n"
        "2. Convert a PFX certificate to PEM.\n"
        "3. Generate a CSR (will create a private key if one does not exist).\n"
        "4. Generate a PEM certificate (requires CSR).\n\n"
        "Enter choice: "
    )

    if choice == "1":
        pem_to_pfx()
    elif choice == "2":
        pfx_to_pem()
    elif choice == "3":
        generate_csr()
    elif choice == "4":
        generate_pem()
    else:
        print("Your selection didn't match any options.")
        sys.exit(1)


if __name__ == "__main__":
    main()