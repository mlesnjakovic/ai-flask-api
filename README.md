# AI Revenue Predictor

Ovaj projekt koristi **strojno učenje (Machine Learning)** kako bi predvidio **povećanje prihoda tvrtke (%)** temeljem primjene umjetne inteligencije.

---

## Što model predviđa?

Model predviđa:
> **Koliko će se prihod povećati (%) zahvaljujući implementaciji AI-a u poslovanje.**

### Primjer:
Ako unesete:
- **AI Adoption Rate (%)**: `70`
- **AI-Generated Content Volume (TBs/year)**: `100`
- **Job Loss Due to AI (%)**: `10`
- **Human-AI Collaboration Rate (%)**: `60`
- **Consumer Trust in AI (%)**: `80`
- **Market Share of AI Companies (%)**: `25`

Model će vratiti nešto poput:
```
{"prediction": 34.2}
```

---

## Ulazne značajke (features)

| Parametar | Objašnjenje |
|----------|-------------|
| `AI Adoption Rate (%)` | Postotak usvojenosti AI tehnologije |
| `AI-Generated Content Volume` | Količina sadržaja generiranog AI-em (u terabajtima godišnje) |
| `Job Loss Due to AI (%)` | Procijenjeni postotak izgubljenih radnih mjesta zbog AI-a |
| `Human-AI Collaboration Rate (%)` | Koliko ljudi surađuje s AI-jem u radu |
| `Consumer Trust in AI (%)` | Povjerenje potrošača u AI |
| `Market Share of AI Companies (%)` | Tržišni udio AI-orijentiranih tvrtki |

---

## Tehnologije

- Python 3.11
- Flask (API)
- scikit-learn (model treniran)
- joblib (spremanje modela)
- HTML + JS (frontend)
- Render.com (cloud hosting)

---

## Online pristup

**Prilikom prvog pokretanja `ai_predikcija.html` potrebno je malo duže pričekati dok se model "probudi", svakim idućim pokretanjem odziv je brži

