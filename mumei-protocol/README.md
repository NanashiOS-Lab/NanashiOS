# Mumei Protocol 👻🔒

**Registre décentralisé d’authenticité et de provenance**  
**pour les agents IA souverains de NanashiOS**

**Pas de nom. Pas de trace. Contrôle total.**

---

### Qu’est-ce que Mumei Protocol ?

Mumei est le **protocole de confiance décentralisé** qui permet à l’écosystème Nanashi IA de fonctionner sans cloud tout en garantissant l’authenticité et l’intégrité des agents.

Il répond à une question critique :  
**Comment savoir qu’un agent téléchargé depuis la marketplace n’a pas été altéré, censuré ou malveillant ?**

Mumei résout cela via un **registre immuable on-chain** sur un subnet Bittensor dédié, avec vérification décentralisée (Proof of Intelligence) sans jamais compromettre l’exécution 100 % locale.

---

### Fonctionnalités principales

- **Registre on-chain immuable** : hash, version, métadonnées et certificat d’authenticité de chaque agent
- **Proof of Intelligence (PoI)** : vérification décentralisée par miners et validators du subnet Bittensor
- **Challenges multiples** : benchmarks, simulations comportementales, détection watermark C2PA, analyse de code statique
- **Consensus Yuma** : scoring robuste et résistant à la collusion
- **Privacy renforcée** : ε-differential privacy pendant la vérification
- **Intégration transparente** avec NanashiOS : vérification locale du certificat avant téléchargement
- **Économie incitative** : rewards en TAO + $NANA pour les participants au subnet

---

### Architecture globale

```mermaid
flowchart TD
    Dev[Développeur] -->|1. Soumet agent| SC[Smart Contract Mumei]
    SC -->|2. Déclenche challenges| SN[Subnet Bittensor Mumei]
    SN --> Miner[Miners<br>exécutent benchmarks + simulations]
    Miner --> Validator[Validators<br>scorent via consensus Yuma]
    Validator -->|3. Consensus| CERT[Certificat généré]
    CERT --> SC
    SC --> REG[Registre on-chain<br>hash + certificat]
    User[Utilisateur] -->|4. Vérifie certificat| REG
    REG -->|Certificat valide| NS[NanashiOS<br>exécution 100 % locale]
