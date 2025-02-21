from .backend.quiz import QuizType

quizzes = {
    # World
    "WORLD": {
        "quizzes": [

        ],
        "regions": {

        }
    },

    # Africa
    "AFR": {
        "quizzes": [
            {
                "quiz-id": "afr-countries",
                "quiz-name": _("Countries"),
                "quiz-type": QuizType.REGIONS,
                "map": "africa",
                "items": ["AO", "BF", "BI", "BJ", "BW", "CD", "CF", "CG", "CI", "CM", "DJ", "DZ", "EG", "ER", "ET", "GA", "GH", "GM", "GN", "GQ", "GW", "KE", "LR", "LS", "LY", "MA", "MG", "ML", "MR", "MW", "MZ", "NA", "NE", "NG", "RW", "SD", "SL", "SN", "SO", "SS", "SZ", "TD", "TG", "TN", "TZ", "UG", "ZA", "ZM", "ZW"]
            },
            {
                "quiz-id": "afr-capitals",
                "quiz-name": _("Capitals"),
                "quiz-type": QuizType.CAPITALS,
                "map": "africa",
                "items": ["AO", "BF", "BI", "BJ", "BW", "CD", "CF", "CG", "CI", "CM", "DJ", "DZ", "EG", "ER", "ET", "GA", "GH", "GM", "GN", "GQ", "GW", "KE", "LR", "LS", "LY", "MA", "MG", "ML", "MR", "MW", "MZ", "NA", "NE", "NG", "RW", "SD", "SL", "SN", "SO", "SS", "SZ", "TD", "TG", "TN", "TZ", "UG", "ZA", "ZM", "ZW"]
            },
        ],
        "regions": {

        }
    },

    # North America
    "AMN": {
        "quizzes": [
            {
                "quiz-id": "amn-countries",
                "quiz-name": _("Countries"),
                "quiz-type": QuizType.REGIONS,
                "map": "north-america",
                "items": []
            }
        ],
        "regions": {

        }
    },

    # South America
    "AMS": {
        "quizzes": [
            {
                "quiz-id": "ams-countries",
                "quiz-name": _("Countries"),
                "quiz-type": QuizType.REGIONS,
                "map": "south-america",
                "items": []
            }
        ],
        "regions": {

        }
    },

    # Asia
    "AS": {
        "quizzes": [
            {
                "quiz-id": "as-countries",
                "quiz-name": _("Countries"),
                "quiz-type": QuizType.REGIONS,
                "map": "asia",
                "items": []
            }
        ],
        "regions": {

        }
    },

    # Australia
    "AU": {
        "quizzes": [
            {
                "quiz-id": "au-states-territories",
                "quiz-name": _("States and Territories"),
                "quiz-type": QuizType.REGIONS,
                "map": "australia",
                "items": ["AU-ACT", "AU-NSW", "AU-NT", "AU-QLD", "AU-SA", "AU-TAS", "AU-VIC", "AU-WA"]
            },
            {
                "quiz-id": "au-states-territories-capitals",
                "quiz-name": _("States and Territories: Capitals"),
                "quiz-type": QuizType.CAPITALS,
                "map": "australia",
                "items": ["AU-ACT", "AU-NSW", "AU-NT", "AU-QLD", "AU-SA", "AU-TAS", "AU-VIC", "AU-WA"]
            }
        ],
        "regions": {

        }
    },

    # Europe
    "EU": {
        "quizzes": [
            {
                "quiz-id": "eu-countries",
                "quiz-name": _("Countries"),
                "quiz-type": QuizType.REGIONS,
                "map": "europe",
                "items": ["AD", "AL", "AM", "AT", "AX", "AZ", "BA", "BE", "BG", "BY", "CH", "CY", "CZ", "DE", "DK", "EE", "ES", "FI", "FO", "FR", "GB", "GE", "GG", "GI", "GR", "HR", "HU", "IE", "IM", "IS", "IT", "JE", "KV", "KZ", "LI", "LT", "LU", "LV", "MC", "MD", "ME", "MK", "MT", "NL", "NO", "PL", "PT", "RO", "RS", "RU", "SE", "SI", "SJ", "SK", "SM", "TR", "UA", "VA"]
            },
            {
                "quiz-id": "eu-countries-capitals",
                "quiz-name": _("Capitals"),
                "quiz-type": QuizType.CAPITALS,
                "map": "europe",
                "items": []
            },
        ],
        "regions": {
            "DE": [
                {
                    "quiz-id": "de-states",
                    "quiz-name": _("States"),
                    "quiz-type": QuizType.REGIONS,
                    "map": "germany",
                    "items": ["DE-BW","DE-BY","DE-BE","DE-BB","DE-HB","DE-HH","DE-HE","DE-MV","DE-NI","DE-NW","DE-RP","DE-SL","DE-SN","DE-ST","DE-SH","DE-TH"]
                },
                {
                    "quiz-id": "de-states-capitals",
                    "quiz-name": _("States: Capitals"),
                    "quiz-type": QuizType.CAPITALS,
                    "map": "germany",
                    "items": ["DE-BW","DE-BY","DE-BE","DE-BB","DE-HB","DE-HH","DE-HE","DE-MV","DE-NI","DE-NW","DE-RP","DE-SL","DE-SN","DE-ST","DE-SH","DE-TH"]
                },
            ],
            "DK": [
                {
                    "quiz-id": "dk-regions",
                    "quiz-name": _("Regions"),
                    "quiz-type": QuizType.REGIONS,
                    "map": "denmark",
                    "items": ["DK-84","DK-82","DK-81","DK-85","DK-83"],
                },
            ],
            "ES": [
                {
                    "quiz-id": "es-autonomies",
                    "quiz-name": _("Autonomies"),
                    "quiz-type": QuizType.REGIONS,
                    "map": "spain-autonomies",
                    "items": ["ES-AN","ES-AR","ES-AS","ES-CB","ES-CE","ES-CL","ES-CM","ES-CN","ES-CT","ES-EX","ES-GA","ES-IB","ES-MC","ES-MD","ES-ML","ES-NC","ES-PV","ES-RI","ES-VC"],
                },
                {
                    "quiz-id": "es-autonomies-capitals",
                    "quiz-name": _("Autonomies: Capitals"),
                    "quiz-type": QuizType.CAPITALS,
                    "map": "spain-autonomies",
                    "items": ["ES-AN","ES-AR","ES-AS","ES-CB","ES-CL","ES-CM","ES-CN","ES-CT","ES-EX","ES-GA","ES-IB","ES-MC","ES-MD","ES-NC","ES-PV","ES-RI","ES-VC"],
                },
                {
                    "quiz-id": "es-provinces",
                    "quiz-name": _("Provinces"),
                    "quiz-type": QuizType.REGIONS,
                    "map": "spain-provinces",
                    "items": ["ES-A","ES-AB","ES-AL","ES-AV","ES-B","ES-BA","ES-BI","ES-BU","ES-C","ES-CA","ES-CC","ES-CO","ES-CR","ES-CS","ES-CU","ES-GC","ES-GI","ES-GR","ES-GU","ES-H","ES-HU","ES-J","ES-L","ES-LE","ES-LO","ES-LU","ES-M","ES-MA","ES-MU","ES-NA","ES-O","ES-OR","ES-P","ES-PM","ES-PO","ES-S","ES-SA","ES-SE","ES-SG","ES-SO","ES-SS","ES-TE","ES-TF","ES-TO","ES-T","ES-V","ES-VA","ES-VI","ES-Z","ES-ZA"],
                },
                {
                    "quiz-id": "es-provinces-capitals",
                    "quiz-name": _("Provinces: Capitals"),
                    "quiz-type": QuizType.CAPITALS,
                    "map": "spain-provinces",
                    "items": ["ES-A","ES-AB","ES-AL","ES-AV","ES-B","ES-BA","ES-BI","ES-BU","ES-C","ES-CA","ES-CC","ES-CO","ES-CR","ES-CS","ES-CU","ES-GC","ES-GI","ES-GR","ES-GU","ES-H","ES-HU","ES-J","ES-L","ES-LE","ES-LO","ES-LU","ES-M","ES-MA","ES-MU","ES-NA","ES-O","ES-OR","ES-P","ES-PM","ES-PO","ES-S","ES-SA","ES-SE","ES-SG","ES-SO","ES-SS","ES-TE","ES-TF","ES-TO","ES-T","ES-V","ES-VA","ES-VI","ES-Z","ES-ZA"],
                },
            ],
            "NL": [
                {
                    "quiz-id": "nl-provinces",
                    "quiz-name": _("Provinces"),
                    "quiz-type": QuizType.REGIONS,
                    "map": "netherlands",
                    "items": ["NL-DR","NL-FL","NL-FR","NL-GE","NL-GR","NL-LI","NL-NB","NL-NH","NL-OV","NL-UT","NL-ZE","NL-ZH"]
                },
                {
                    "quiz-id": "nl-capitals",
                    "quiz-name": _("Capitals"),
                    "quiz-type": QuizType.CAPITALS,
                    "map": "netherlands",
                    "items": ["NL-DR","NL-FL","NL-FR","NL-GE","NL-GR","NL-LI","NL-NB","NL-NH","NL-OV","NL-UT","NL-ZE","NL-ZH"]
                },
            ],
            "NO": [
                {
                    "quiz-id": "no-counties",
                    "quiz-name": _("Counties"),
                    "quiz-type": QuizType.REGIONS,
                    "map": "norway",
                    "items": ["NO-01", "NO-02", "NO-03", "NO-04", "NO-05", "NO-06", "NO-07", "NO-08", "NO-09", "NO-10", "NO-11", "NO-12", "NO-14", "NO-15", "NO-16", "NO-17", "NO-18", "NO-19", "NO-20"],
                },
            ],
            "SE": [
                {
                    "quiz-id": "se-regions",
                    "quiz-name": _("Regions"),
                    "quiz-type": QuizType.REGIONS,
                    "map": "sweden",
                    "items": ["SE-AB", "SE-AC", "SE-BD", "SE-C", "SE-D", "SE-E", "SE-F", "SE-G", "SE-H", "SE-I", "SE-K", "SE-M", "SE-N", "SE-O", "SE-S", "SE-T", "SE-U", "SE-W", "SE-X", "SE-Y", "SE-Z"],
                },
                {
                    "quiz-id": "se-regions-capitals",
                    "quiz-name": _("Regions: Capitals"),
                    "quiz-type": QuizType.CAPITALS,
                    "map": "sweden",
                    "items": ["SE-AB", "SE-AC", "SE-BD", "SE-C", "SE-D", "SE-E", "SE-F", "SE-G", "SE-H", "SE-I", "SE-K", "SE-M", "SE-N", "SE-O", "SE-S", "SE-T", "SE-U", "SE-W", "SE-X", "SE-Y", "SE-Z"],
                },
            ],
        }
    },
}