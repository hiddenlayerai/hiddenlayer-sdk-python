# Changelog

## 3.2.1 (2026-01-09)

Full Changelog: [v3.2.0...v3.2.1](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/compare/v3.2.0...v3.2.1)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([edaab09](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/edaab09f6ae593763951d5167ea9bd3296917a8d))
* use async_to_httpx_files in patch method ([d19fe1b](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/d19fe1bb26b29e5d524ff1ed2604f364dc101411))


### Chores

* add missing docstrings ([a003642](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/a003642e26bbbb022dc14fc8904496ddfdea6a92))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([38c130d](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/38c130d0a716a10c3e2c210a1ae8754b25be4096))
* **internal:** add `--fix` argument to lint script ([c64b851](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/c64b851f4ca661550ecc8177f3713e2f1044be51))
* **internal:** add missing files argument to base client ([b02afa8](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/b02afa86a0292e7af08f187afec2b962c9bb91e9))
* **internal:** codegen related update ([6ad2609](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/6ad260961a7da75a7052b7692b3d952399efb214))
* update lockfile ([79a938e](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/79a938eb5e985ee98181a489c3fc0003891f82b4))


### Documentation

* add more examples ([139e807](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/139e8077775666aeeb935984de40d3d9d4044d32))

## 3.2.0 (2025-12-04)

Full Changelog: [v3.1.0...v3.2.0](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/compare/v3.1.0...v3.2.0)

### Features

* **api:** api update ([6526012](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/6526012dd2f88ad1e42daf6111cc45cea1c0f3af))
* **api:** api update ([f240a44](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/f240a447c1409192586e2dd19d37ff5e9e7ff18f))
* **api:** api update ([82355df](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/82355df0b06543f86991b8219152f59895e03a9c))
* **api:** api update ([c6bdab7](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/c6bdab747bce2549021cc03f0beaac490e539928))
* **api:** api update ([91e4095](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/91e40959b4c85f8d01205389c9b7410cc008b79f))
* **api:** api update ([4531c76](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/4531c76a0badbbee8c2fedf10a23871b9ad8fb10))


### Bug Fixes

* **client:** close streams without requiring full consumption ([c6dcaab](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/c6dcaab8858c9a20470d98d0c0d1523466d83570))
* compat with Python 3.14 ([a26a44c](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/a26a44c343765da9bd9f58dcf29a7af49738c605))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([1ef085f](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/1ef085f82040b406b8aa9501f2a6cafb5819c8fc))
* ensure streams are always closed ([0690ffd](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/0690ffd5784f3118199f4901a4272fd0e5a71dda))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([8181a06](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/8181a06f0f483e25e6db869e12294da5a6966a3a))
* **internal:** codegen related update ([45bc981](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/45bc98170b1ba23b6de8edba2e50d5f96b2ec40f))
* **internal:** grammar fix (it's -&gt; its) ([20dbdf5](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/20dbdf5377db585e380c061a2194a57fcbe28907))
* **package:** drop Python 3.8 support ([4115a5c](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/4115a5c863431d2c1af697c9e9a20f5d46f41d54))

## 3.1.0 (2025-10-22)

Full Changelog: [v3.0.1...v3.1.0](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/compare/v3.0.1...v3.1.0)

### Features

* **api:** api update ([f9b04a6](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/f9b04a6f32744afdfafa6bac6dc8e6cc514ad735))
* **api:** api update ([cac77ff](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/cac77ffde9e844dbaa0089e33d365fb6f01ad060))
* **api:** api update ([a5f4aa4](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/a5f4aa47ae06afd63a0a5f476023492e23b01d87))
* **api:** api update ([f8ea9b3](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/f8ea9b34e18900b9955ce810e396a9050a5a3683))
* **api:** api update ([a09c23c](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/a09c23c700f049b0b20a50bd7b09737981eebe4d))
* **api:** api update ([144ea2b](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/144ea2b7fb99d892088bc72a725fd8a0fecb0382))
* **api:** api update ([495bc26](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/495bc26f2f5aee49e6ac239011a1e9666f9c8e58))
* **api:** api update ([82bcadd](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/82bcaddd193d4ad155eb2651cb190a4a200800e1))
* **api:** api update ([da69d10](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/da69d104dc5f408a04d46c0266973fe404665cf8))
* **api:** api update ([75a179e](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/75a179e93a759b83194806b4c561ad4035ae2714))
* **api:** api update ([56ec98d](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/56ec98d2485b1ebb16a832d4eac125d05a7a1993))
* **api:** manual updates ([7e16b74](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/7e16b749a22db9414de5faf17067f15cf37ff78a))
* **api:** manual updates ([4a1d8af](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/4a1d8af69e44413809219221e5a3ff3b102a7637))
* **api:** restore ScanReport ([5bba48d](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/5bba48def63831679f3f33475b9ed423c9726bbf))


### Bug Fixes

* **compat:** compat with `pydantic&lt;2.8.0` when using additional fields ([a055406](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/a055406b415d42d8b99284a200eaf0af694e14c3))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([01ab00d](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/01ab00ddaf35da51b7c4a546c37f7d092357ffe4))
* **internal:** detect missing future annotations with ruff ([e087ecc](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/e087ecc97867d858d138af0ebb7dfd7e919c14bb))

## 3.0.1 (2025-09-23)

Full Changelog: [v3.0.0...v3.0.1](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/compare/v3.0.0...v3.0.1)

### Features

* **api:** manual updates ([2be2f2c](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/2be2f2c124d8ac9b9d22c675c165be496c1793ba))

## 3.0.0 (2025-09-23)

Full Changelog: [v0.1.0-alpha.33...v3.0.0](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/compare/v0.1.0-alpha.33...v3.0.0)

### Chores

* update SDK settings ([d72d6b1](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/d72d6b163b84905c9772a97c73acf93a0b14e850))

## 0.1.0-alpha.33 (2025-09-23)

Full Changelog: [v0.1.0-alpha.32...v0.1.0-alpha.33](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/compare/v0.1.0-alpha.32...v0.1.0-alpha.33)

### Features

* **api:** add function for getting the JWT to help with auth ([2241969](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/22419698ee0da7065e42903753d033b0a6bce54c))
* **api:** api update ([79c778d](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/79c778d140f52ded1fcca54847619a3e66679b28))
* **api:** api update ([2820209](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/28202095eaebe32167155c5faa4de21ca55c8cf0))
* **api:** api update ([e3f1144](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/e3f1144d0e00e094460d5f3c38cd696d8e2c16ab))
* **api:** api update ([0b76e66](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/0b76e66357ab10abb39f66a020117832dc506d16))
* **api:** api update ([545e9af](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/545e9af1c1cf3da2d8054d1721e3f2513b33f07c))
* **api:** api update ([4db1715](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/4db1715172e71f9b6a74794cea907359a7d96857))
* **api:** api update ([82c11fa](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/82c11fa6610e8f5dba2688767afb59fbfc61425d))
* **api:** api update ([beff32c](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/beff32cfc1c6007662c1e379c29aa8e83e87c840))
* **api:** api update ([f09759f](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/f09759f30636ee203b3fda40e35ce83f2aa0168d))
* **api:** api update ([021184c](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/021184c0ded6cb982542594a096e0998cbdb8fde))
* **api:** api update ([d84b79e](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/d84b79ee8775415404386844eaace22ac17ad83d))
* **api:** api update ([367ecb5](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/367ecb595cb729696c90e04a1740ff42573510c9))
* **api:** api update ([92606a2](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/92606a2d8f3e242e40119ebd3234ae06d05dcbea))
* **api:** manual updates ([4e7ae89](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/4e7ae891898ecf0894200543406c69002d89dc74))
* **api:** manual updates ([1fbbe1e](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/1fbbe1ed0bd99897a568f92ab1707140ff313753))
* **api:** manual updates ([09f3e8e](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/09f3e8eee58ac5967af4d53cf6c6dc7e505fdea9))
* **api:** manual updates ([1744bae](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/1744bae7b54cc3362eed103f3351016f1e490946))
* **api:** manual updates ([4d57655](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/4d5765535a776f5e109457de67fd1306a6a93eed))
* **api:** manual updates ([61c01c3](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/61c01c3eec14a94987775265a3b8ba990b6b2d26))
* **api:** manual updates ([504fb70](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/504fb708ee7aa8f5b1d5f63632756035cec6ed70))
* **api:** manual updates ([b8b0a6a](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/b8b0a6a090d3a448af989a5518834a0d39f6cb7b))
* **api:** manual updates ([e520ec7](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/e520ec71e6704a4f9776ec172f1f5a69b37de4b1))
* **api:** manual updates ([c831240](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/c831240cec0e47c320016af8dddf95cb38e8c59b))
* **api:** manual updates ([c578b41](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/c578b41dc6cb6829922068672672d344a90f784c))
* **api:** update python production repo ([439b1a8](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/439b1a838166994c6463738d0699f256453274f3))
* **api:** update security to override to Bearer ([0ee703c](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/0ee703c0bfde7ea23e99502c6a404664766a8d34))
* **api:** update via SDK Studio ([ed57dcd](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/ed57dcd64e8bb109d2eeb43860253019732aac5d))
* **api:** update via SDK Studio ([8863e61](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/8863e6140c0dbecc02951b0bebdd4d2410a780dc))


### Bug Fixes

* **package:** support direct resource imports ([8c35192](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/8c35192644c4921ae7ef1dd3f8b8ced673f41fcf))
* **parsing:** correctly handle nested discriminated unions ([e52f99d](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/e52f99da532b2437aa5641a49aa17baa7c8f0e4a))
* **pydantic v1:** more robust ModelField.annotation check ([66ea37a](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/66ea37abf8cf30afb399dac27ab9b20ff9239e81))


### Chores

* **api:** remove unneeded files ([#50](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/issues/50)) ([e0e6e2b](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/e0e6e2bf8f87b82e30eb177b241a9c7913d49cce))
* broadly detect json family of content-type headers ([3df70db](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/3df70db5dc08bab75a9615ee5e5fa3ca985069d7))
* **ci:** add timeout thresholds for CI jobs ([9313327](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/93133273c8c86aacce264b38b319d8b21d2f0ad1))
* **ci:** fix installation instructions ([4127677](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/4127677b77a590fdb0fe10fffae8eb429a8cdc0b))
* **ci:** only use depot for staging repos ([758db79](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/758db7957c47763c859fa74d4a8fe6aa867113a8))
* **ci:** upload sdks to package manager ([b3c7382](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/b3c7382dbdb9a5f278b0bcf0e3409cf11fffe47a))
* configure new SDK language ([28b963b](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/28b963bd6a2c83b02d10d62414743271e83c7422))
* **internal:** avoid errors for isinstance checks on proxies ([3fb2e73](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/3fb2e73fae3388d8d6122ecc046ef64756c05864))
* **internal:** base client updates ([2c8e872](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/2c8e872ce0f712546d835cbb17db2f00851c7cb8))
* **internal:** bump pinned h11 dep ([f67609b](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/f67609b05c128b0e7f52ef85d31125d430ac4616))
* **internal:** bump pyright version ([4db92ef](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/4db92ef2f9773987c2abb473242d6acf0b887167))
* **internal:** codegen related update ([a10bc88](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/a10bc88d1542f573b58c81e616c48cc6da6c8a0e))
* **internal:** codegen related update ([d38c7bb](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/d38c7bb197c1f229fdbd31eb1dd86e20b98df6e1))
* **internal:** codegen related update ([f62836c](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/f62836cdbfc5871425b0f743349cc53bfb7aed14))
* **internal:** fix list file params ([7edb408](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/7edb4080770c52cb2aa450aa716f0099f48bd608))
* **internal:** import reformatting ([797c931](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/797c931eeea9b13e10d157d15e9075d18b4ff188))
* **internal:** minor formatting changes ([8a6ee86](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/8a6ee867788bd228bc6d3bcbe2694179c9075d84))
* **internal:** refactor retries to not use recursion ([b4a79b6](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/b4a79b6b82c3537a8d42593ff6f24166fcca217a))
* **internal:** update models test ([9b4b63e](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/9b4b63e95aed827cea45c88abc4b4314ac46274b))
* **package:** mark python 3.13 as supported ([ece5123](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/ece51230519f8299569d9d77b15b3a264d1fd1e1))
* **readme:** fix version rendering on pypi ([d2cf18b](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/commit/d2cf18b0fd49629033a17b515f2a3adaa6ccab57))

## 0.1.0-alpha.32 (2025-09-19)

Full Changelog: [v0.1.0-alpha.31...v0.1.0-alpha.32](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.31...v0.1.0-alpha.32)

### Features

* **api:** api update ([a91887d](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/a91887d7f2d6022be03a9840684c8f16733fbff4))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([f84656f](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/f84656fbf20f36b2c9b68c393cd615fcb84649aa))

## 0.1.0-alpha.31 (2025-09-19)

Full Changelog: [v0.1.0-alpha.30...v0.1.0-alpha.31](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.30...v0.1.0-alpha.31)

### Features

* **api:** api update ([d782a16](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/d782a1623c60f12276d659b4ec2920cb019a464a))
* **api:** api update ([8a382c3](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/8a382c3b03866edd63304969f2c5ecf89ed70749))

## 0.1.0-alpha.30 (2025-09-18)

Full Changelog: [v0.1.0-alpha.29...v0.1.0-alpha.30](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.29...v0.1.0-alpha.30)

## 0.1.0-alpha.29 (2025-09-18)

Full Changelog: [v0.1.0-alpha.28...v0.1.0-alpha.29](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.28...v0.1.0-alpha.29)

### Features

* **api:** api update ([6472e4e](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/6472e4e38cdba10f8e6495bbd7c6da53c7165db0))


### Chores

* **types:** change optional parameter type from NotGiven to Omit ([724a3f5](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/724a3f51dfe3e25c73474f799fb0e07352eabbfe))

## 0.1.0-alpha.28 (2025-09-17)

Full Changelog: [v0.1.0-alpha.27...v0.1.0-alpha.28](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.27...v0.1.0-alpha.28)

### Chores

* **api:** remove unneeded files ([#50](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/issues/50)) ([e0e6e2b](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/e0e6e2bf8f87b82e30eb177b241a9c7913d49cce))

## 0.1.0-alpha.27 (2025-09-17)

Full Changelog: [v0.1.0-alpha.26...v0.1.0-alpha.27](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.26...v0.1.0-alpha.27)

### Features

* **api:** add Interactions endpoint ([dde9346](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/dde9346d35bbad61dbc108f14b982750e7031a96))
* **api:** add models for Interactions ([90e3bf1](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/90e3bf1a5235578723be8518829623f2609fb226))
* **api:** additional Interactions models ([8853eb3](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/8853eb317e31f642dfc3d8d98367131b5a743926))
* **api:** api update ([7e3f0ea](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/7e3f0ea87cc0ea5db73dc72051946cf5b00451c5))


### Bug Fixes

* **api:** drop Interactions Project model ([a4f3c6d](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/a4f3c6dacd62455ec6917c7d5ac21ae3fc928867))
* **api:** ensure correct HiddenLayer branding ([db14bba](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/db14bba1281cda6b8bd294f433eb1f400f8a8b76))
* **api:** properly namespace Interactions models ([ae8cbf7](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/ae8cbf798bed8dd7f7ee513dfc63c8f7aab7969f))
* **api:** remove all Interactions models ([8c049b0](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/8c049b0f5262d9b7ac805dd81ccd5bc0a13de37e))
* **api:** rename Interactions project model ([1a4a26c](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/1a4a26c4eee075b7cb7d194c52c59367c38822f0))
* **api:** set `default_env_prefix` to `HIDDENLAYER` in `client_settings` ([84a46a5](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/84a46a5dddc47e22c15b29b3bdd2a633066dfd43))
* **docs:** update docs url ([3314a6f](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/3314a6f7b7024c67dc866d9ed2c0a82feb74859c))


### Chores

* **internal:** update pydantic dependency ([a5b0e2e](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/a5b0e2eb759d7b327f4f415da6268081f488ddb5))

## 0.1.0-alpha.26 (2025-09-15)

Full Changelog: [v0.1.0-alpha.25...v0.1.0-alpha.26](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.25...v0.1.0-alpha.26)

### Features

* **api:** add sarif route ([337a430](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/337a4304e42008593296ef8084ea6b6f4453f709))

## 0.1.0-alpha.25 (2025-09-12)

Full Changelog: [v0.1.0-alpha.24...v0.1.0-alpha.25](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.24...v0.1.0-alpha.25)

### Features

* **api:** update tokenUrl ([cdc49d2](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/cdc49d29f21227398522bf7b388dcc573d27aebd))


### Chores

* **tests:** simplify `get_platform` test ([9f9d70c](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/9f9d70cc86012175becee389a438572560fef8e6))

## 0.1.0-alpha.24 (2025-09-11)

Full Changelog: [v0.1.0-alpha.23...v0.1.0-alpha.24](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.23...v0.1.0-alpha.24)

### Features

* improve future compat with pydantic v3 ([1aed84f](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/1aed84fc565e40734f229cf1ee2d86d7152f670a))


### Chores

* **internal:** move mypy configurations to `pyproject.toml` file ([ba5e158](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/ba5e1586993c00ec16aeb3195d4aae3ab8859bf7))

## 0.1.0-alpha.23 (2025-09-02)

Full Changelog: [v0.1.0-alpha.22...v0.1.0-alpha.23](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.22...v0.1.0-alpha.23)

### Features

* **api:** api update ([0192f46](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/0192f465bdabc8204a0889040502017c227cd4f3))
* **types:** replace List[str] with SequenceNotStr in params ([a5e1c2a](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/a5e1c2ac52a81996654d05931917fd0aec4ca7b6))

## 0.1.0-alpha.22 (2025-08-29)

Full Changelog: [v0.1.0-alpha.21...v0.1.0-alpha.22](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.21...v0.1.0-alpha.22)

### Features

* **api:** api update ([f523d38](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/f523d38d325d7289203b06c3d1e5243f654b283f))


### Chores

* **internal:** add Sequence related utils ([f0af51b](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/f0af51badaf337f14b0a64663f97f1d0a3b9976e))
* **internal:** update pyright exclude list ([6f11796](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/6f1179674007bbe5fd140204492223b4d35854f6))

## 0.1.0-alpha.21 (2025-08-26)

Full Changelog: [v0.1.0-alpha.20...v0.1.0-alpha.21](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.20...v0.1.0-alpha.21)

### Bug Fixes

* avoid newer type syntax ([2450326](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/2450326713c4b1363ce61096389623aed9a3fc5f))


### Chores

* **internal:** change ci workflow machines ([0184a6c](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/0184a6cc5a54c83c36a498d7cbcc32789db3b3be))
* **internal:** codegen related update ([2924314](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/29243141ec253dc932eafc66533f5e9e741cca99))
* **internal:** update comment in script ([1552b01](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/1552b0178410fc7b06edfaae412c41b282b3dcb5))
* update @stainless-api/prism-cli to v5.15.0 ([49e15d5](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/49e15d59663269cf65d53ed967dbca173707f1e8))
* update github action ([8aa456b](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/8aa456b76cc854b3419198adf8e544bab8bfaffe))

## 0.1.0-alpha.20 (2025-08-07)

Full Changelog: [v0.1.0-alpha.19...v0.1.0-alpha.20](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.19...v0.1.0-alpha.20)

### Features

* **api:** remove create /api/v2/models ([d2d1103](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/d2d110327ce164c9ace4747e0da49c162a12ffde))

## 0.1.0-alpha.19 (2025-08-06)

Full Changelog: [v0.1.0-alpha.18...v0.1.0-alpha.19](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.18...v0.1.0-alpha.19)

### Chores

* **internal:** fix ruff target version ([509ce89](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/509ce8922316e9136e4991a049dd4b22daaa9e88))

## 0.1.0-alpha.18 (2025-08-06)

Full Changelog: [v0.1.0-alpha.17...v0.1.0-alpha.18](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.17...v0.1.0-alpha.18)

## 0.1.0-alpha.17 (2025-08-06)

Full Changelog: [v0.1.0-alpha.16...v0.1.0-alpha.17](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.16...v0.1.0-alpha.17)

## 0.1.0-alpha.16 (2025-08-05)

Full Changelog: [v0.1.0-alpha.15...v0.1.0-alpha.16](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.15...v0.1.0-alpha.16)

## 0.1.0-alpha.15 (2025-08-04)

Full Changelog: [v0.1.0-alpha.14...v0.1.0-alpha.15](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.14...v0.1.0-alpha.15)

## 0.1.0-alpha.14 (2025-07-31)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

## 0.1.0-alpha.13 (2025-07-31)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Features

* **api:** api update ([ab856d6](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/ab856d679d1886feb580ae99b79790ab511a125c))
* **api:** manual updates ([f926e12](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/f926e12f4ed77fa2777c354944e03f28c98fd989))
* **api:** remove model intel routes ([dff1d61](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/dff1d610507c2ecbac95b4c195d78d7494f68c3f))
* **client:** support file upload requests ([c00c3a0](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/c00c3a0f8bc1ab385d6f7e7895cf1033cc5d3dcc))


### Chores

* remove custom code ([aa328cc](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/aa328ccd2f408272249035c3fdbc5728e5e1cd49))

## 0.1.0-alpha.12 (2025-07-25)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Features

* **api:** manual updates ([03fdded](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/03fddedb61bda77435ade41ffdc7286295dac2f1))


### Chores

* **project:** add settings file for vscode ([d6407aa](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/d6407aae7256cb72bdb447f3e6fd20ee36d12119))

## 0.1.0-alpha.11 (2025-07-23)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Features

* **api:** manual updates ([83758c8](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/83758c8f08d6cf44413d8703da5c170e29751a6a))

## 0.1.0-alpha.10 (2025-07-23)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Bug Fixes

* **parsing:** parse extra field types ([c62653d](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/c62653dcbd61315c94430b5cc155051e4c0f6cbb))

## 0.1.0-alpha.9 (2025-07-22)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** api update ([e86ec2d](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/e86ec2d17d3918f698fea2e7b809ad3ca9d47c0b))

## 0.1.0-alpha.8 (2025-07-22)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** api update ([5e105bc](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/5e105bc648ffd9e084494d327ee7399ad5079f43))

## 0.1.0-alpha.7 (2025-07-22)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** api update ([2433e73](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/2433e73b7c551f02db091efb9af210632f0032cd))


### Bug Fixes

* **parsing:** ignore empty metadata ([f3b496b](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/f3b496b5f48e4bd6aa38ab260c76cface06bea8a))


### Chores

* **types:** rebuild Pydantic models after all types are defined ([186ccda](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/186ccda280184623ff694cdbce1eae5c98e57aa9))

## 0.1.0-alpha.6 (2025-07-18)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** added PUT /api/v2/models to config ([d2be4c9](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/d2be4c99d166db198c902efe6e9430b7ded0d270))

## 0.1.0-alpha.5 (2025-07-17)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** api update ([5aee97f](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/5aee97f2d8baa684f1b83c9db4df274fc2ce3548))

## 0.1.0-alpha.4 (2025-07-17)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** added sensor update ([6a77a18](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/6a77a187141a0775d7a50c268205ce1be99e82fc))

## 0.1.0-alpha.3 (2025-07-16)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

## 0.1.0-alpha.2 (2025-07-16)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

## 0.1.0-alpha.1 (2025-07-15)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** add function for getting the JWT to help with auth ([2241969](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/22419698ee0da7065e42903753d033b0a6bce54c))
* **api:** added offset-page pagination scheme ([6e98ef8](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/6e98ef832b83450ad4fed47c1e4a23fb9bfb0922))
* **api:** api update ([7a4683b](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/7a4683b104d18b815a829cdb0e8d01ca56280262))
* **api:** api update ([0b76e66](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/0b76e66357ab10abb39f66a020117832dc506d16))
* **api:** api update ([545e9af](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/545e9af1c1cf3da2d8054d1721e3f2513b33f07c))
* **api:** api update ([4db1715](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/4db1715172e71f9b6a74794cea907359a7d96857))
* **api:** api update ([82c11fa](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/82c11fa6610e8f5dba2688767afb59fbfc61425d))
* **api:** api update ([beff32c](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/beff32cfc1c6007662c1e379c29aa8e83e87c840))
* **api:** api update ([f09759f](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/f09759f30636ee203b3fda40e35ce83f2aa0168d))
* **api:** api update ([021184c](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/021184c0ded6cb982542594a096e0998cbdb8fde))
* **api:** api update ([d84b79e](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/d84b79ee8775415404386844eaace22ac17ad83d))
* **api:** api update ([367ecb5](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/367ecb595cb729696c90e04a1740ff42573510c9))
* **api:** api update ([92606a2](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/92606a2d8f3e242e40119ebd3234ae06d05dcbea))
* **api:** manual updates ([7e068b5](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/7e068b527b5ec5de48660db3dc7834b0dbd19944))
* **api:** manual updates ([09f3e8e](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/09f3e8eee58ac5967af4d53cf6c6dc7e505fdea9))
* **api:** manual updates ([1744bae](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/1744bae7b54cc3362eed103f3351016f1e490946))
* **api:** manual updates ([4d57655](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/4d5765535a776f5e109457de67fd1306a6a93eed))
* **api:** manual updates ([61c01c3](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/61c01c3eec14a94987775265a3b8ba990b6b2d26))
* **api:** manual updates ([504fb70](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/504fb708ee7aa8f5b1d5f63632756035cec6ed70))
* **api:** manual updates ([b8b0a6a](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/b8b0a6a090d3a448af989a5518834a0d39f6cb7b))
* **api:** manual updates ([e520ec7](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/e520ec71e6704a4f9776ec172f1f5a69b37de4b1))
* **api:** manual updates ([c831240](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/c831240cec0e47c320016af8dddf95cb38e8c59b))
* **api:** manual updates ([c578b41](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/c578b41dc6cb6829922068672672d344a90f784c))
* **api:** update security to override to Bearer ([0ee703c](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/0ee703c0bfde7ea23e99502c6a404664766a8d34))
* **api:** update via SDK Studio ([ed57dcd](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/ed57dcd64e8bb109d2eeb43860253019732aac5d))
* **api:** update via SDK Studio ([8863e61](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/8863e6140c0dbecc02951b0bebdd4d2410a780dc))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([7e4a8b8](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/7e4a8b8200d9c0caeb2bd94ffc24167a62aa0ff5))
* **package:** support direct resource imports ([8c35192](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/8c35192644c4921ae7ef1dd3f8b8ced673f41fcf))
* **parsing:** correctly handle nested discriminated unions ([e52f99d](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/e52f99da532b2437aa5641a49aa17baa7c8f0e4a))
* **pydantic v1:** more robust ModelField.annotation check ([66ea37a](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/66ea37abf8cf30afb399dac27ab9b20ff9239e81))


### Chores

* broadly detect json family of content-type headers ([3df70db](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/3df70db5dc08bab75a9615ee5e5fa3ca985069d7))
* **ci:** add timeout thresholds for CI jobs ([9313327](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/93133273c8c86aacce264b38b319d8b21d2f0ad1))
* **ci:** fix installation instructions ([4127677](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/4127677b77a590fdb0fe10fffae8eb429a8cdc0b))
* **ci:** only use depot for staging repos ([758db79](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/758db7957c47763c859fa74d4a8fe6aa867113a8))
* **ci:** upload sdks to package manager ([b3c7382](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/b3c7382dbdb9a5f278b0bcf0e3409cf11fffe47a))
* configure new SDK language ([28b963b](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/28b963bd6a2c83b02d10d62414743271e83c7422))
* **internal:** avoid errors for isinstance checks on proxies ([3fb2e73](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/3fb2e73fae3388d8d6122ecc046ef64756c05864))
* **internal:** base client updates ([2c8e872](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/2c8e872ce0f712546d835cbb17db2f00851c7cb8))
* **internal:** bump pinned h11 dep ([f67609b](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/f67609b05c128b0e7f52ef85d31125d430ac4616))
* **internal:** bump pyright version ([4db92ef](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/4db92ef2f9773987c2abb473242d6acf0b887167))
* **internal:** codegen related update ([a10bc88](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/a10bc88d1542f573b58c81e616c48cc6da6c8a0e))
* **internal:** codegen related update ([d38c7bb](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/d38c7bb197c1f229fdbd31eb1dd86e20b98df6e1))
* **internal:** codegen related update ([f62836c](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/f62836cdbfc5871425b0f743349cc53bfb7aed14))
* **internal:** fix list file params ([7edb408](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/7edb4080770c52cb2aa450aa716f0099f48bd608))
* **internal:** import reformatting ([797c931](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/797c931eeea9b13e10d157d15e9075d18b4ff188))
* **internal:** minor formatting changes ([8a6ee86](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/8a6ee867788bd228bc6d3bcbe2694179c9075d84))
* **internal:** refactor retries to not use recursion ([b4a79b6](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/b4a79b6b82c3537a8d42593ff6f24166fcca217a))
* **internal:** update models test ([9b4b63e](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/9b4b63e95aed827cea45c88abc4b4314ac46274b))
* **package:** mark python 3.13 as supported ([ece5123](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/ece51230519f8299569d9d77b15b3a264d1fd1e1))
* **readme:** fix version rendering on pypi ([d2cf18b](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/d2cf18b0fd49629033a17b515f2a3adaa6ccab57))
* update SDK settings ([345840c](https://github.com/hiddenlayer-engineering/hiddenlayer-sdk-python/commit/345840cfaec887645d112636bde1b1a88374a4b6))
