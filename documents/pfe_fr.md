# Titre  : 
CLAP-RAP-FR : Modèle Multimodal Modulaire pour l’Analyse du Rap Français et la Recommandation Musicale Émotionnelle

# Résumé
Ce Projet de Fin d’Études vise à développer un modèle multimodal innovant basé sur l’architecture CLAP (Contrastive Language–Audio Pretraining), entièrement spécialisé pour le rap français. L’objectif est de créer une base d’intelligence artificielle capable de comprendre le contenu audio, le style, les paroles et les émotions propres au rap francophone, puis de construire un système de recommandation musicale basé sur les émotions ressenties par l’utilisateur.

Le projet explore également une extension moderne et modulaire du modèle via l’intégration de techniques avancées de LoRA (Low-Rank Adaptation) et de Mixture-of-Experts (MoE) afin de permettre l’ajout illimité de nouvelles compétences au modèle (nouveaux sous-genres, émotions, styles, artistes), sans nécessiter de réentraîner l’ensemble de l’architecture.

# 🎯 Objectifs

Construire un modèle CLAP spécialisé pour le rap français, capable d’apprendre simultanément :

- la structure audio (flow, rythmique, production…)

- les paroles et leur sémantique

- les émotions et thèmes du rap français

Constituer un dataset multimodal inédit :

- extraits audio de rap FR

- paroles (lyrics)

- annotations émotionnelles (mélancolie, égotrip, storytelling, rage, chill…)

- sous-genres (drill FR, trap, cloud, old-school, afro-trap, etc.)

Mettre en place une architecture modulaire basée sur :

- un CLAP-Core gelé qui joue le rôle de base générale

- des LoRA adapters pour ajouter facilement de nouvelles connaissances

- une couche Mixture-of-Experts (MoE) pour spécialiser automatiquement le modèle selon le sous-genre ou le type d’émotion

Concevoir un système de recommandation musicale émotionnelle :

- l’utilisateur exprime un état émotionnel (“motivation”, “mélancolie”, “rage”, “chill”)

- le système génère les morceaux les plus pertinents dans l’espace embedding du CLAP-RAP-FR

- Évaluer scientifiquement le modèle :

- retrieval audio ↔ texte ↔ émotion

- classification d’émotions

- reconnaissance de sous-genres

- étude utilisateur pour valider la qualité de la recommandation

🧠 Innovation

Le projet est scientifiquement original car :

- Aucun CLAP n’est spécialisé pour le rap français.

- L’intégration de LoRA + MoE dans un modèle multimodal audio/texte est nouvelle dans ce domaine.

- Le système de recommandation émotionnelle basé sur un espace CLAP spécialisé rap FR est inédit.

- Le modèle devient extensible à l’infini sans réentraînement global.

Ce PFE se situe à l’intersection du deep learning multimodal, de la music information retrieval (MIR) et du traitement audio moderne, tout en s’adressant à un domaine culturel spécifique.

# 🔧 Méthodologie (résumé)

- Extraction d’un dataset audio (20–30 secondes/morceau)

- Récupération de paroles via APIs

- Annotation des émotions

- Entraînement du CLAP-RAP-FR

- Congélation du modèle de base

- Ajout d'experts MoE pour différents styles et émotions

- Ajout de LoRA pour affiner certains comportements

- Construction de l’index vectoriel FAISS pour la recommandation

- Évaluation et validation

# 📌 Livrables

- Modèle CLAP-RAP-FR préentraîné

- Module MoE spécialisé sous-genres & émotions

- Adapters LoRA modulaires

- Dataset multimodal rap FR annoté

- Système complet de recommandation émotionnelle

- Rapport + démonstration

# 🚀 Impact

Ce projet ouvre la voie à :

- des systèmes de recommandation plus sensibles à la culture musicale locale,

- des modèles audio/texte modulaires facilement extensibles,

- de nouvelles applications dans la production musicale, le streaming et l’analyse automatique du rap.

