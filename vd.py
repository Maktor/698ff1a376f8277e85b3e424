import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_hickory_venn_diagram():

    fig, ax = plt.subplots(figsize=(10, 10))

    fig.patch.set_facecolor('#E6E6E6')
    ax.set_facecolor('#E6E6E6')

    circle_settings = [
        {'center': (0.35, 0.6), 'radius': 0.35},  # Top Left
        {'center': (0.65, 0.6), 'radius': 0.35},  # Top Right
        {'center': (0.5, 0.35), 'radius': 0.35}   # Bottom
    ]

    for circle in circle_settings:
        c = patches.Circle(
            circle['center'],
            circle['radius'],
            linewidth=6,
            edgecolor='black',
            facecolor='none'
        )
        ax.add_patch(c)

    text_elements = [
        (0.20, 0.70, 'H', 'black', 35),
        (0.15, 0.60, 'K', 'black', 35),
        (0.28, 0.55, 'T', 'blue', 35),
        (0.24, 0.78, 'Z', 'black', 35),

        (0.80, 0.70, 'Q', 'black', 35),
        (0.85, 0.60, 'C', 'black', 35),
        (0.72, 0.56, 'G', 'black', 35), # Mostly curve
        (0.76, 0.79, 'S', 'black', 35),

        (0.50, 0.10, 'α', 'black', 40), # Alpha
        (0.40, 0.14, 'λ', 'black', 40), # Lambda
        (0.60, 0.20, 'τ', 'black', 40), # Tau
        (0.48, 0.24, 'ν', 'green', 40), # Nu

        (0.50, 0.75, 'P', 'black', 35), # Straight line + Curve
        (0.50, 0.62, 'D', 'red', 35),   # Straight line + Curve
        (0.53, 0.55, 'J', 'black', 35),

        (0.30, 0.44, 'Δ', 'black', 40), # Delta (Straight lines)
        (0.35, 0.32, 'Σ', 'black', 40), # Sigma (Straight lines)

        (0.70, 0.45, 'θ', 'black', 40), # Theta (Curved)
        (0.65, 0.32, 'ρ', 'black', 40), # Rho (Curved/Mixed depending on font, usually fits here)
        (0.75, 0.35, 'β', 'black', 40), # Beta (Curved)
    ]

    for x, y, char, color, size in text_elements:
        ax.text(
            x, y, char,
            color=color,
            fontsize=size,
            ha='center',
            va='center',
            fontfamily='serif',
            fontweight='bold'
        )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create_hickory_venn_diagram()
