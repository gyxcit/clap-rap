# Title: 
CLAP-RAP-FR: A Modular Multimodal Model for French Rap Analysis and Emotion-Based Music Recommendation

# Abstract

This Final Year Project aims to develop an innovative multimodal model based on the CLAP (Contrastive Language–Audio Pretraining) architecture, fully specialized for French rap. The goal is to build an AI system capable of understanding audio content, lyrical meaning, stylistic features, and emotional characteristics specific to francophone rap, and then to use this model to build an emotion-driven music recommendation system.

The project also explores the integration of modern modular learning techniques, including LoRA (Low-Rank Adaptation) and Mixture-of-Experts (MoE), to enable the model to be extended with an unlimited number of new skills or domains (new subgenres, emotions, vocal styles, artists) without requiring full retraining of the core model.

# 🎯 Objectives

Develop a CLAP model specialized in French rap, capable of learning:

- audio structure (flow, rhythm patterns, production style)

- lyrical semantics and slang

- emotional and thematic content specific to French rap

- Build a novel multimodal dataset, including:

- French rap audio excerpts

- lyrics

- emotional annotations (melancholy, rage, ego-trip, storytelling, chill…)

- subgenre labels (French drill, trap, cloud rap, old school, afro-trap, etc.)

Create a modular architecture composed of:

- a frozen CLAP-Core acting as a general base model

- LoRA adapters for lightweight incremental learning

- a Mixture-of-Experts (MoE) layer to automatically specialize the model based on emotion or subgenre

- Design an emotion-based music recommendation system, where:

- the user provides an emotional state (“motivated”, “melancholic”, “angry”, “chill”)

- the system retrieves the most relevant French rap tracks from the CLAP embedding space

- Evaluate the model scientifically through:

- audio ↔ text ↔ emotion retrieval tasks

- emotion recognition

- subgenre classification

- user study for recommendation quality

# 🧠 Innovation

This project is scientifically novel because:

- No existing CLAP model is specialized in French rap.

- Combining LoRA + MoE within a multimodal audio–text framework is new in this field.

- The emotion-driven recommendation engine built on a specialized CLAP space is unique.

- The architecture supports unlimited extension without retraining the core model.

- The PFE sits at the intersection of multimodal deep learning, Music Information Retrieval (MIR), and modern audio processing, while focusing on a culturally rich and under-explored domain.

# 🔧 Methodology (Summary)

- Collect & extract audio clips (20–30s)

- Retrieve lyrics via public APIs

- Annotate emotional labels

- Train the CLAP-RAP-FR model

- Freeze the core model

- Add MoE experts for subgenres & emotions

- Add LoRA adapters for fine-grained improvements

- Build a FAISS vector index for recommendation

- Evaluate and validate performance

# 📌 Deliverables

- Pretrained CLAP-RAP-FR model

- MoE expert modules

- LoRA adapter modules

- Annotated multimodal French rap dataset

- Fully functional emotion-based recommendation system

- Final report + demonstration

🚀 Impact

This project paves the way for:

- culturally-aware and emotion-sensitive music recommendation systems,

- modular and extensible multimodal neural architectures,

- new applications in audio analysis, music production, and streaming platforms.