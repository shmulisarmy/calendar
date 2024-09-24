const January = new Map([
    [1, {
        "day": 1,
        "day of week": "Sunday",
        events: [
            {
                "name": "Birthday",
                "startTime": "10:00",
                "endTime": "11:00",
                "description": "My birthday!"
            },
            {
                "name": "Breakfast",
                "startTime": "11:00",
                "endTime": "12:00",
                "description": "I need to eat food!"
            }
        ]
    }],
    [2, {
        "day": 2,
        "day of week": "Monday",
        events: [
            {
                "name": "Morning Run",
                "startTime": "06:30",
                "endTime": "07:30",
                "description": "Start the day with a 5km run."
            },
            {
                "name": "Team Meeting",
                "startTime": "09:00",
                "endTime": "10:30",
                "description": "Project update meeting with the team."
            },
            {
                "name": "Lunch",
                "startTime": "12:00",
                "endTime": "13:00",
                "description": "Grab a quick lunch with colleagues."
            }
        ]
    }],
    [3, {
        "day": 3,
        "day of week": "Tuesday",
        events: [
            {
                "name": "Gym Workout",
                "startTime": "07:00",
                "endTime": "08:00",
                "description": "Weight training session."
            },
            {
                "name": "Client Presentation",
                "startTime": "10:00",
                "endTime": "11:30",
                "description": "Presenting project results to the client."
            }
        ]
    }],
    [4, {
        "day": 4,
        "day of week": "Wednesday",
        events: [
            {
                "name": "Yoga",
                "startTime": "06:30",
                "endTime": "07:30",
                "description": "Morning yoga session."
            },
            {
                "name": "Coding Session",
                "startTime": "09:00",
                "endTime": "12:00",
                "description": "Work on the new feature implementation."
            },
            {
                "name": "Lunch with Friend",
                "startTime": "13:00",
                "endTime": "14:00",
                "description": "Catch up over lunch."
            }
        ]
    }],
    [5, {
        "day": 5,
        "day of week": "Thursday",
        events: [
            {
                "name": "Marketing Workshop",
                "startTime": "09:00",
                "endTime": "11:00",
                "description": "Attend marketing strategy workshop."
            },
            {
                "name": "Dentist Appointment",
                "startTime": "15:00",
                "endTime": "16:00",
                "description": "Regular dental check-up."
            }
        ]
    }],
    [6, {
        "day": 6,
        "day of week": "Friday",
        events: [
            {
                "name": "Grocery Shopping",
                "startTime": "09:30",
                "endTime": "10:30",
                "description": "Stock up for the weekend."
            },
            {
                "name": "Team Lunch",
                "startTime": "12:00",
                "endTime": "13:00",
                "description": "Lunch outing with the team."
            },
            {
                "name": "Game Night",
                "startTime": "18:00",
                "endTime": "21:00",
                "description": "Board games with friends."
            }
        ]
    }],
    [7, {
        "day": 7,
        "day of week": "Saturday",
        events: [
            {
                "name": "Cleaning",
                "startTime": "10:00",
                "endTime": "12:00",
                "description": "Weekly house cleaning."
            },
            {
                "name": "Movie Night",
                "startTime": "20:00",
                "endTime": "23:00",
                "description": "Watch a new release with family."
            }
        ]
    }],
    [8, {
            "day": 8,
            "day of week": "Sunday",
            events: [
                {
                    "name": "Brunch with Family",
                    "startTime": "10:30",
                    "endTime": "12:00",
                    "description": "Sunday brunch at home."
                },
                {
                    "name": "Afternoon Hike",
                    "startTime": "14:00",
                    "endTime": "16:00",
                    "description": "Hiking at the local park."
                }
            ]
        }],
        [9, {
            "day": 9,
            "day of week": "Monday",
            events: [
                {
                    "name": "Morning Meditation",
                    "startTime": "06:00",
                    "endTime": "06:30",
                    "description": "Start the week with a clear mind."
                },
                {
                    "name": "Work on Presentation",
                    "startTime": "09:00",
                    "endTime": "11:00",
                    "description": "Prepare slides for the upcoming conference."
                },
                {
                    "name": "Client Call",
                    "startTime": "14:00",
                    "endTime": "15:00",
                    "description": "Discuss project updates with the client."
                }
            ]
        }],
        [10, {
            "day": 10,
            "day of week": "Tuesday",
            events: [
                {
                    "name": "Gym Session",
                    "startTime": "07:00",
                    "endTime": "08:00",
                    "description": "Cardio and strength training."
                },
                {
                    "name": "Team Standup",
                    "startTime": "10:00",
                    "endTime": "10:30",
                    "description": "Daily standup with the dev team."
                },
                {
                    "name": "Dinner with Friend",
                    "startTime": "19:00",
                    "endTime": "21:00",
                    "description": "Catch up with an old friend."
                }
            ]
        }],
        [11, {
            "day": 11,
            "day of week": "Wednesday",
            events: [
                {
                    "name": "Yoga Class",
                    "startTime": "06:30",
                    "endTime": "07:30",
                    "description": "Mid-week yoga session."
                },
                {
                    "name": "Project Deadline",
                    "startTime": "09:00",
                    "endTime": "17:00",
                    "description": "Final submission for the client project."
                }
            ]
        }],
        [12, {
            "day": 12,
            "day of week": "Thursday",
            events: [
                {
                    "name": "Morning Walk",
                    "startTime": "07:00",
                    "endTime": "08:00",
                    "description": "Walk in the neighborhood park."
                },
                {
                    "name": "Work Meeting",
                    "startTime": "09:00",
                    "endTime": "10:00",
                    "description": "Quarterly planning with the team."
                },
                {
                    "name": "Coffee with Client",
                    "startTime": "15:00",
                    "endTime": "16:00",
                    "description": "Meet a client to discuss new opportunities."
                }
            ]
        }],
        [13, {
            "day": 13,
            "day of week": "Friday",
            events: [
                {
                    "name": "Grocery Run",
                    "startTime": "08:00",
                    "endTime": "09:00",
                    "description": "Pick up groceries for the weekend."
                },
                {
                    "name": "Coding Sprint",
                    "startTime": "10:00",
                    "endTime": "13:00",
                    "description": "Intense coding session to push features."
                },
                {
                    "name": "Movie Night",
                    "startTime": "19:00",
                    "endTime": "21:00",
                    "description": "Watch a new release on Netflix."
                }
            ]
        }],
        [14, {
            "day": 14,
            "day of week": "Saturday",
            events: [
                {
                    "name": "Cleaning",
                    "startTime": "09:00",
                    "endTime": "11:00",
                    "description": "Weekend house cleaning."
                },
                {
                    "name": "Lunch Out",
                    "startTime": "12:30",
                    "endTime": "14:00",
                    "description": "Eat out at a local restaurant."
                },
                {
                    "name": "Reading",
                    "startTime": "16:00",
                    "endTime": "17:00",
                    "description": "Finish reading the book."
                }
            ]
        }],
        [15, {
            "day": 15,
            "day of week": "Sunday",
            events: [
                {
                    "name": "Church Service",
                    "startTime": "09:00",
                    "endTime": "10:00",
                    "description": "Attend church service."
                },
                {
                    "name": "Family BBQ",
                    "startTime": "12:00",
                    "endTime": "15:00",
                    "description": "BBQ lunch with family."
                }
            ]
        }],
        [16, {
            "day": 16,
            "day of week": "Monday",
            events: [
                {
                    "name": "Morning Run",
                    "startTime": "06:00",
                    "endTime": "07:00",
                    "description": "Start the week with a run."
                },
                {
                    "name": "Work on Blog",
                    "startTime": "10:00",
                    "endTime": "12:00",
                    "description": "Write new content for the blog."
                },
                {
                    "name": "Dinner with Parents",
                    "startTime": "18:30",
                    "endTime": "20:00",
                    "description": "Have dinner with parents."
                }
            ]
        }],
            // Previous entries for days 1 and 8-16
            // Now adding 17-29, excluding 8-16
            [17, {
                "day": 17,
                "day of week": "Tuesday",
                events: [
                    {
                        "name": "Team Meeting",
                        "startTime": "09:00",
                        "endTime": "10:00",
                        "description": "Weekly sync with the team."
                    },
                    {
                        "name": "Coding Practice",
                        "startTime": "14:00",
                        "endTime": "16:00",
                        "description": "Leetcode coding practice."
                    }
                ]
            }],
            [18, {
                "day": 18,
                "day of week": "Wednesday",
                events: [
                    {
                        "name": "Workout",
                        "startTime": "07:00",
                        "endTime": "08:00",
                        "description": "Strength training at the gym."
                    },
                    {
                        "name": "Project Review",
                        "startTime": "11:00",
                        "endTime": "12:00",
                        "description": "Review project status with the manager."
                    }
                ]
            }],
            [19, {
                "day": 19,
                "day of week": "Thursday",
                events: [
                    {
                        "name": "Grocery Shopping",
                        "startTime": "08:00",
                        "endTime": "09:00",
                        "description": "Buy groceries for the week."
                    },
                    {
                        "name": "Webinar",
                        "startTime": "15:00",
                        "endTime": "16:30",
                        "description": "Attend a webinar on web development."
                    }
                ]
            }],
            [20, {
                "day": 20,
                "day of week": "Friday",
                events: [
                    {
                        "name": "Morning Meditation",
                        "startTime": "06:00",
                        "endTime": "06:30",
                        "description": "End the week with a peaceful mind."
                    },
                    {
                        "name": "Client Call",
                        "startTime": "10:00",
                        "endTime": "11:00",
                        "description": "Discuss project feedback with the client."
                    }
                ]
            }],
            [21, {
                "day": 21,
                "day of week": "Saturday",
                events: [
                    {
                        "name": "Weekend Hike",
                        "startTime": "08:00",
                        "endTime": "10:00",
                        "description": "Hike at the local trail."
                    },
                    {
                        "name": "Lunch with Friends",
                        "startTime": "13:00",
                        "endTime": "15:00",
                        "description": "Catch up with friends over lunch."
                    }
                ]
            }],
            [22, {
                "day": 22,
                "day of week": "Sunday",
                events: [
                    {
                        "name": "Brunch with Family",
                        "startTime": "10:00",
                        "endTime": "12:00",
                        "description": "Sunday brunch with family."
                    },
                    {
                        "name": "Relax",
                        "startTime": "14:00",
                        "endTime": "16:00",
                        "description": "Relax and unwind with a good book."
                    }
                ]
            }],
            [23, {
                "day": 23,
                "day of week": "Monday",
                events: [
                    {
                        "name": "Morning Yoga",
                        "startTime": "06:00",
                        "endTime": "07:00",
                        "description": "Start the week with yoga."
                    },
                    {
                        "name": "Work on Assignment",
                        "startTime": "10:00",
                        "endTime": "13:00",
                        "description": "Complete work assignment."
                    }
                ]
            }],
            [24, {
                "day": 24,
                "day of week": "Tuesday",
                events: [
                    {
                        "name": "Doctor's Appointment",
                        "startTime": "09:00",
                        "endTime": "10:00",
                        "description": "Regular checkup."
                    },
                    {
                        "name": "Work on Side Project",
                        "startTime": "11:00",
                        "endTime": "14:00",
                        "description": "Continue working on a side coding project."
                    }
                ]
            }],
            [25, {
                "day": 25,
                "day of week": "Wednesday",
                events: [
                    {
                        "name": "Morning Jog",
                        "startTime": "07:00",
                        "endTime": "08:00",
                        "description": "Mid-week jog in the park."
                    },
                    {
                        "name": "Team Brainstorming",
                        "startTime": "10:00",
                        "endTime": "11:30",
                        "description": "Brainstorming session with the team."
                    }
                ]
            }],
            [26, {
                "day": 26,
                "day of week": "Thursday",
                events: [
                    {
                        "name": "Client Presentation",
                        "startTime": "09:00",
                        "endTime": "10:00",
                        "description": "Present project progress to the client."
                    },
                    {
                        "name": "Work on Article",
                        "startTime": "11:00",
                        "endTime": "13:00",
                        "description": "Write a technical blog article."
                    }
                ]
            }],
            [27, {
                "day": 27,
                "day of week": "Friday",
                events: [
                    {
                        "name": "Morning Swim",
                        "startTime": "07:00",
                        "endTime": "08:00",
                        "description": "Swim at the community pool."
                    },
                    {
                        "name": "Team Lunch",
                        "startTime": "12:00",
                        "endTime": "13:00",
                        "description": "Team bonding over lunch."
                    }
                ]
            }],
            [28, {
                "day": 28,
                "day of week": "Saturday",
                events: [
                    {
                        "name": "Weekend Getaway",
                        "startTime": "09:00",
                        "endTime": "17:00",
                        "description": "Day trip to the mountains."
                    },
                    {
                        "name": "Dinner with Friends",
                        "startTime": "19:00",
                        "endTime": "21:00",
                        "description": "Dinner at a local restaurant."
                    }
                ]
            }],
            [29, {
                "day": 29,
                "day of week": "Sunday",
                events: [
                    {
                        "name": "Church Service",
                        "startTime": "09:00",
                        "endTime": "10:00",
                        "description": "Attend church."
                    },
                    {
                        "name": "Relax and Read",
                        "startTime": "15:00",
                        "endTime": "16:00",
                        "description": "Spend the afternoon reading."
                    }
                ]
            }]
        
    
]);
