import matplotlib.pyplot as plt
import numpy as np

binary_data = "010110010110111101110101001001110111001001100101001000000110000101101100011011000010000001001001001000000110010101110110011001010111001000100000011011100110010101100101011001000110010101100100001011000010000001111001011001010110000101101000"

# ============================================================
# 1. UNIPOLAR NRZ
# Bit 1 -> +V
# Bit 0 -> 0V
# ============================================================

def unipolar_nrz(binary_str):
    """Encodes a binary string using Unipolar NRZ line coding."""
    # Convert string of '0'/'1' into a list of integers
    bit_stream = [int(bit) for bit in binary_str]
    return bit_stream

# ============================================================
# 2. POLAR NRZ-L
# Bit 1 -> -V
# Bit 0 -> +V
# ============================================================

def polar_nrz_l(binary_str):

    """Encodes a binary string using Polar NRZ-L line coding."""

    bit_stream = []

    for bit in binary_str:

        if bit == '1':
            bit_stream.append(-1)
        else:
            bit_stream.append(1)

    return bit_stream


# ============================================================
# 3. POLAR NRZ-I
# Bit 1 -> change
# Bit 0 -> no change
# ============================================================

def polar_nrz_i(binary_str):

    """Encodes a binary string using Polar NRZ-I line coding."""

    bit_stream = []

    current_level = 1

    for bit in binary_str:

        # Bit 1 causes a transition
        if bit == '1':
            current_level *= -1

        # Bit 0 causes no transition
        bit_stream.append(current_level)

    return bit_stream


# ============================================================
# 4. POLAR RZ
# Bit 1 -> starts at +V, then returns to 0
# Bit 0 -> starts at -V, then returns to 0
# ============================================================

def polar_rz(binary_str):

    """Encodes a binary string using Polar RZ line coding."""

    bit_stream = []

    for bit in binary_str:

        if bit == '1':
            bit_stream.append(1)
            bit_stream.append(0)

        else:
            bit_stream.append(-1)
            bit_stream.append(0)

    return bit_stream


# ============================================================
# 5. POLAR BIPHASE (MANCHESTER)
# Bit 1 -> -V then +V
# Bit 0 -> +V then -V
# ============================================================

def manchester(binary_str):

    """Encodes a binary string using Manchester line coding."""

    bit_stream = []

    for bit in binary_str:

        if bit == '1':
            bit_stream.append(-1)
            bit_stream.append(1)

        else:
            bit_stream.append(1)
            bit_stream.append(-1)

    return bit_stream


# ============================================================
# 6. POLAR BIPHASE (DIFFERENTIAL MANCHESTER)
# Bit 1 -> no transition at beginning
# Bit 0 -> transition at beginning
# Middle of every bit -> transition
# ============================================================

def differential_manchester(binary_str):

    """Encodes a binary string using Differential Manchester."""

    bit_stream = []

    current_level = 1

    for bit in binary_str:

        # Bit 0 causes a transition at the beginning
        if bit == '0':
            current_level *= -1

        # First half of bit
        bit_stream.append(current_level)

        # Mandatory middle transition
        current_level *= -1

        # Second half of bit
        bit_stream.append(current_level)

    return bit_stream


# ============================================================
# 7. BIPOLAR AMI
# Bit 0 -> 0V
# Bit 1 -> alternates between +V and -V
# ============================================================

def bipolar_ami(binary_str):

    """Encodes a binary string using Bipolar AMI."""

    bit_stream = []

    current_level = -1

    for bit in binary_str:

        if bit == '0':
            bit_stream.append(0)

        else:
            # Alternate between +V and -V
            current_level *= -1
            bit_stream.append(current_level)

    return bit_stream


# ============================================================
# 8. BIPOLAR PSEUDOTERNARY
# Bit 1 -> 0V
# Bit 0 -> alternates between +V and -V
# ============================================================

def bipolar_pseudoternary(binary_str):

    """Encodes a binary string using Bipolar Pseudoternary."""

    bit_stream = []

    current_level = -1

    for bit in binary_str:

        if bit == '1':
            bit_stream.append(0)

        else:
            # Alternate between +V and -V
            current_level *= -1
            bit_stream.append(current_level)

    return bit_stream


# ============================================================
# ENCODE THE BINARY DATA
# ============================================================

sig_unipolar = unipolar_nrz(binary_data)

sig_nrz_l = polar_nrz_l(binary_data)

sig_nrz_i = polar_nrz_i(binary_data)

sig_rz = polar_rz(binary_data)

sig_manchester = manchester(binary_data)

sig_diff_manchester = differential_manchester(binary_data)

sig_ami = bipolar_ami(binary_data)

sig_pseudoternary = bipolar_pseudoternary(binary_data)


# ============================================================
# PLOTTING FUNCTION
# ============================================================

def plot_signal(binary_str, encode_function, title, values_per_bit=1):

    max_bits = 60

    for start in range(0, len(binary_str), max_bits):

        bits = binary_str[start:start + max_bits]

        signal = encode_function(bits)

        plt.figure(figsize=(18, 4))

        plt.plot(
            signal,
            drawstyle="steps-post",
            linewidth=2.5
        )

        plt.ylim(-1.2, 1.2)

        plt.title(
            f"{title} (Bits {start + 1}-{start + len(bits)})"
        )

        plt.xlabel("Bit Interval")

        plt.ylabel("Amplitude (V)")

        plt.grid(True)

        # Display binary bits
        for i, bit in enumerate(bits):

            plt.text(
                i * values_per_bit + values_per_bit / 2,
                1.05,
                bit,
                ha="center",
                fontsize=8
            )

        plt.show()


# ============================================================
# PLOT ALL 8 LINE ENCODING SCHEMES
# ============================================================
# 1 value per bit
plot_signal(binary_data, unipolar_nrz, "1. Unipolar NRZ")
plot_signal(binary_data, polar_nrz_l, "2. Polar NRZ-L")
plot_signal(binary_data, polar_nrz_i, "3. Polar NRZ-I")
plot_signal(binary_data, bipolar_ami, "7. Bipolar AMI")
plot_signal(binary_data, bipolar_pseudoternary, "8. Bipolar Pseudoternary")

# 2 values per bit
plot_signal(binary_data, polar_rz, "4. Polar RZ", 2)
plot_signal(binary_data, manchester, "5. Polar Biphase (Manchester)", 2)
plot_signal(binary_data, differential_manchester, "6. Polar Biphase (Differential Manchester)", 2)