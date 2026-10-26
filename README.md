<p align="center">
  <img src="assets/readme/banner.jpg" alt="التعلّم المعزّز العميق: كورس Hugging Face بالعربي" width="100%">
</p>

<p align="center">
  <img alt="Course" src="https://img.shields.io/badge/course-Hugging%20Face%20Deep%20RL-ffcc4d?style=flat-square&logo=huggingface&logoColor=black">
  <img alt="Language" src="https://img.shields.io/badge/%D8%A7%D9%84%D8%B4%D8%B1%D8%AD-%D8%B9%D8%B1%D8%A8%D9%8A-2a78d6?style=flat-square">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776ab?style=flat-square&logo=python&logoColor=white">
  <img alt="Colab" src="https://img.shields.io/badge/run%20on-Google%20Colab-f9ab00?style=flat-square&logo=googlecolab&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-52514e?style=flat-square">
</p>

## عن الريبو

هنا نوتبوكس كورس [Hugging Face Deep Reinforcement Learning](https://huggingface.co/learn/deep-rl-course) بالشرح العربي.
كل نوتبوكس متشغّلة من أولها لآخرها، والنتايج الحقيقية محفوظة جواها: الأرقام، والرسوم، وفيديوهات الـ `agent` وهو بيلعب.
الشرح بالعربي، والمصطلحات بالإنجليزي زي ما هتلاقيها في أي مرجع أو كود.

كل نوتبوكس ليها حلقة فيديو بتشرحها خطوة بخطوة، والروابط هتتضاف جنب كل وحدة أول ما تتنشر.

## الخطة

| الوحدة | الموضوع | المشروع | الحالة |
|---|---|---|---|
| 0 | مقدمة الكورس | تجهيز البيئة | ⏳ قريبًا |
| 1 | أساسيات `Deep RL` | `LunarLander` بـ `PPO` و `Stable-Baselines3` | ⏳ قريبًا |
| بونص 1 | `Huggy` | تدريب كلب `Huggy` بـ `Unity ML-Agents` | ⏳ قريبًا |
| 2 | `Q-Learning` | `FrozenLake` و `Taxi` من الصفر | ⏳ قريبًا |
| 3 | `Deep Q-Learning` | `Space Invaders` من `Atari` | ⏳ قريبًا |
| بونص 2 | ضبط الـ `hyperparameters` | `Optuna` | ⏳ قريبًا |
| 4 | `Policy Gradient` | `REINFORCE` بـ `PyTorch` على `CartPole` و `Pixelcopter` | ⏳ قريبًا |
| 5 | `Unity ML-Agents` | `SnowballTarget` و `Pyramids` | ⏳ قريبًا |
| 6 | `Actor-Critic` | `A2C` على `panda-gym` | ⏳ قريبًا |
| 7 | `Multi-Agent` و `self-play` | `SoccerTwos` | ⏳ قريبًا |
| 8 | `PPO` | `PPO` من الصفر بـ `CleanRL`، و `Sample Factory` على `ViZDoom` | ⏳ قريبًا |

وبين كل وحدة والتانية فيه نوتبوكس مشروع عملي كامل من الصفر للآخر.

## تشغيل النوتبوكس

أسهل طريقة إنك تفتح النوتبوكس على `Google Colab` وتختار `GPU` من:

```
Runtime → Change runtime type → T4 GPU
```

كل نوتبوكس بتثبّت المكتبات اللي محتاجاها في أول خلية. ولو هتشغّل على جهازك:

```bash
git clone https://github.com/mmmohamedaaashraf/deep-rl-arabic.git
cd deep-rl-arabic
python3 -m venv .venv && source .venv/bin/activate
pip install jupyterlab
jupyter lab
```

## ترتيب الملفات

```
deep-rl-arabic/
├── notebooks/       نوتبوكس كل وحدة في فولدر باسمها (unit1/، unit2/، …)
├── assets/          صور الريبو والخطوط
├── LICENSE          Apache License 2.0
└── NOTICE           مصدر المحتوى الأصلي والتعديلات
```

## المصدر والرخصة

المحتوى مبني على [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course) و
[`huggingface/deep-rl-class`](https://github.com/huggingface/deep-rl-class)، المنشور برخصة `Apache-2.0`.
النوتبوكس هنا مترجمة ومشروحة بالعربي، ومعدّلة ومتشغّلة بنتايجها، والتفاصيل في ملف [`NOTICE`](NOTICE).
الريبو كله منشور برخصة [`Apache-2.0`](LICENSE). خط `Cairo` المستخدم في الصور منشور برخصة `SIL OFL 1.1`.

<p align="center"><sub>Mohamed Ashraf Mostafa · Petroleum & Robotics Engineer</sub></p>
