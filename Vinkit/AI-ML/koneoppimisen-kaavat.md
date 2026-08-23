<!-- tags: vinkit, ai-ml -->

# Koneoppimisen kaavat

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Kymmenen keskeistä koneoppimisen kaavaa. "Aloita ymmärtämällä kaavat jokaisen mallin takana."

## Linear Regression (lineaarinen regressio)

Ennustaa jatkuvia arvoja.

ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ

## Logistic Regression (logistinen regressio)

Ennustaa todennäköisyyksiä luokittelua varten.

P(y=1) = 1 / (1 + e^(−z))

missä z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ

## Gradient Descent (gradienttilaskeutuminen)

Päivittää mallin parametreja.

θ = θ − α · ∂J/∂θ

missä α = oppimisnopeus (learning rate)

## Mean Squared Error – MSE (keskineliövirhe)

Mittaa keskimääräisen neliövirheen.

MSE = (1/n) · Σᵢ₌₁ⁿ (yᵢ − ŷᵢ)²

## Cross Entropy Loss

Käytetään luokitteluongelmissa.

L = −Σᵢ₌₁ⁿ yᵢ · log(ŷᵢ)

## Entropy (entropia)

Mittaa epävarmuutta.

H(S) = −Σᵢ₌₁ⁿ pᵢ · log₂(pᵢ)

## Information Gain (informaatiohyöty)

Käytetään päätöspuissa.

IG = Entropy(Parent) − Σ (|Child|/|Parent|) · Entropy(Child)

## Euclidean Distance (euklidinen etäisyys)

Mittaa etäisyyden kahden pisteen välillä.

d = √( Σᵢ₌₁ⁿ (xᵢ − yᵢ)² )

## Bayes' Theorem (Bayesin teoreema)

Naive Bayesin perusta.

P(C|X) = P(X|C) · P(C) / P(X)

## Softmax Function

Käytetään monen luokan luokittelussa.

P(yᵢ) = e^(zᵢ) / Σⱼ₌₁ⁿ e^(zⱼ)
