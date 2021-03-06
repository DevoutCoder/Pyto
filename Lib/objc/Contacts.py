"""
Classes from the 'Contacts' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


CNContainerDiffCalculator = _Class("CNContainerDiffCalculator")
CNChangeHistoryLabeledValueChange = _Class("CNChangeHistoryLabeledValueChange")
CNSiriIntelligenceSettings = _Class("CNSiriIntelligenceSettings")
CNContactLocationVCardSummary = _Class("CNContactLocationVCardSummary")
CNChangeHistory = _Class("CNChangeHistory")
CNFavorites = _Class("CNFavorites")
CNDowntimeWhitelist = _Class("CNDowntimeWhitelist")
CNCDLog = _Class("CNCDLog")
CNAddressFormats = _Class("CNAddressFormats")
CNSyncImageResult = _Class("CNSyncImageResult")
_CNRegulatoryLogger = _Class("_CNRegulatoryLogger")
CNPredicateValidator = _Class("CNPredicateValidator")
CNMockAPITriageLogger = _Class("CNMockAPITriageLogger")
CNiOSABEKParticipantMatchingSearchOperationDelegate = _Class(
    "CNiOSABEKParticipantMatchingSearchOperationDelegate"
)
CNAPITriageLogger = _Class("CNAPITriageLogger")
CNiOSABConstantsMapping = _Class("CNiOSABConstantsMapping")
CNCFPhoneNumber = _Class("CNCFPhoneNumber")
CNPhoneNumber = _Class("CNPhoneNumber")
CNContainerCache = _Class("CNContainerCache")
_CNContactsLogger = _Class("_CNContactsLogger")
CNContactFetchRequestEffectiveKeyExtender = _Class(
    "CNContactFetchRequestEffectiveKeyExtender"
)
CNMockGeminiLogger = _Class("CNMockGeminiLogger")
CNCountryInformation = _Class("CNCountryInformation")
CNSafeChangeHistoryEventVisitorWrapper = _Class(
    "CNSafeChangeHistoryEventVisitorWrapper"
)
CNDonationMapper = _Class("CNDonationMapper")
CNChangeHistoryAnchor = _Class("CNChangeHistoryAnchor")
_CNChangeHistoryGroupRefillStrategy = _Class("_CNChangeHistoryGroupRefillStrategy")
_CNChangeHistoryContactRefillStrategy = _Class("_CNChangeHistoryContactRefillStrategy")
CNContainerUpdate = _Class("CNContainerUpdate")
CNContactVCardSerialization = _Class("CNContactVCardSerialization")
CNReputationResult = _Class("CNReputationResult")
CNMockContactsLogger = _Class("CNMockContactsLogger")
CNFavoritesEntry = _Class("CNFavoritesEntry")
CNFavoritesLookupChangeRecord = _Class("CNFavoritesLookupChangeRecord")
CNErrorFactory = _Class("CNErrorFactory")
_CNContactMatchingFetchRequestInfos = _Class("_CNContactMatchingFetchRequestInfos")
CNMailToGroup = _Class("CNMailToGroup")
CNiOSABPredicateRunner = _Class("CNiOSABPredicateRunner")
_CNGeminiLogger = _Class("_CNGeminiLogger")
CNiOSFetchExecution = _Class("CNiOSFetchExecution")
_CNContactPhoneNumberEquivalence = _Class("_CNContactPhoneNumberEquivalence")
_CNContactEmailAddressEquivalence = _Class("_CNContactEmailAddressEquivalence")
CNContactHandleIndexableString = _Class("CNContactHandleIndexableString")
CNPostalAddressFormattingSpecification = _Class(
    "CNPostalAddressFormattingSpecification"
)
CNAuthorization = _Class("CNAuthorization")
CNContactDiff = _Class("CNContactDiff")
CNAggregateKeyDescriptor = _Class("CNAggregateKeyDescriptor")
CNContactImageFetchRequest = _Class("CNContactImageFetchRequest")
_CNContactVCardNameSummzarizationScope = _Class(
    "_CNContactVCardNameSummzarizationScope"
)
CNContactVCardSummary = _Class("CNContactVCardSummary")
CNReputationCoreRecentsAdapter = _Class("CNReputationCoreRecentsAdapter")
CNContactMetadataPersistentStoreManager = _Class(
    "CNContactMetadataPersistentStoreManager"
)
CNiOSPersonFetchRequest = _Class("CNiOSPersonFetchRequest")
CNiOSAddressBook = _Class("CNiOSAddressBook")
CNContactMatchInfo = _Class("CNContactMatchInfo")
CNVCardConstantsMapping = _Class("CNVCardConstantsMapping")
CNReputationContactsAdapter = _Class("CNReputationContactsAdapter")
CNGeminiHandle = _Class("CNGeminiHandle")
CNContactChangesNotifier = _Class("CNContactChangesNotifier")
CNContactChangesFetcher = _Class("CNContactChangesFetcher")
CNContactChangesObserverProxy = _Class("CNContactChangesObserverProxy")
CNReputationLogger = _Class("CNReputationLogger")
CNLabelValuePair = _Class("CNLabelValuePair")
CNUuidIdentifierProvider = _Class("CNUuidIdentifierProvider")
CNiOSABDependentPropertiesUpdateContext = _Class(
    "CNiOSABDependentPropertiesUpdateContext"
)
CNContactProperty = _Class("CNContactProperty")
CNReputationHandle = _Class("CNReputationHandle")
_CNReputationPhoneNumberHandle = _Class("_CNReputationPhoneNumberHandle")
_CNReputationEmailAddressHandle = _Class("_CNReputationEmailAddressHandle")
_CNReputationGenericHandle = _Class("_CNReputationGenericHandle")
CNContainerDiff = _Class("CNContainerDiff")
CNDraggingContact = _Class("CNDraggingContact")
CNiOSABConversions = _Class("CNiOSABConversions")
CNContactSubsetCalculator = _Class("CNContactSubsetCalculator")
_CNSpotlightIndexingLogger = _Class("_CNSpotlightIndexingLogger")
CNSmartPropertyFetcher = _Class("CNSmartPropertyFetcher")
CNContactFormatterSmartFetcher = _Class("CNContactFormatterSmartFetcher")
CNSyncImageUtilities = _Class("CNSyncImageUtilities")
CNChangeHistoryEventFactory = _Class("CNChangeHistoryEventFactory")
CN = _Class("CN")
CNContactClassifiedHandleStringInterpreter = _Class(
    "CNContactClassifiedHandleStringInterpreter"
)
CNDonatedContactSanitizer = _Class("CNDonatedContactSanitizer")
CNSaveRequest = _Class("CNSaveRequest")
CNSuggestedSaveRequest = _Class("CNSuggestedSaveRequest")
CNIndexClientState = _Class("CNIndexClientState")
CNChangeHistoryResult = _Class("CNChangeHistoryResult")
CNContactVCardWritingAdapter = _Class("CNContactVCardWritingAdapter")
CNSaveResponse = _Class("CNSaveResponse")
CNMutableSaveResponse = _Class("CNMutableSaveResponse")
CNPhoneDialer = _Class("CNPhoneDialer")
CNContactNameSorting = _Class("CNContactNameSorting")
CNChangeNotifierDistributedCenterWrapper = _Class(
    "CNChangeNotifierDistributedCenterWrapper"
)
CNChangeNotifierDarwinWrapper = _Class("CNChangeNotifierDarwinWrapper")
CNChangesNotifier = _Class("CNChangesNotifier")
CNChangesNotifierProxy = _Class("CNChangesNotifierProxy")
CNValueOrigin = _Class("CNValueOrigin")
CNAccessAuthorization = _Class("CNAccessAuthorization")
CNMockFavoritesLogger = _Class("CNMockFavoritesLogger")
CNContactBufferDecoderFactory = _Class("CNContactBufferDecoderFactory")
CNContainer = _Class("CNContainer")
CNMutableContainer = _Class("CNMutableContainer")
CNSaveRequestVerifier = _Class("CNSaveRequestVerifier")
CNPolicy = _Class("CNPolicy")
CNPermissivePolicy = _Class("CNPermissivePolicy")
CNDictionaryPolicy = _Class("CNDictionaryPolicy")
CNiOSABPolicy = _Class("CNiOSABPolicy")
CNContactRelation = _Class("CNContactRelation")
CNCoreSpotlightSearch = _Class("CNCoreSpotlightSearch")
CNMAIDMapper = _Class("CNMAIDMapper")
CNReputationFutureBuilder = _Class("CNReputationFutureBuilder")
CNContactNameOrderImpl = _Class("CNContactNameOrderImpl")
CNFamilyNameFirstNameOrder = _Class("CNFamilyNameFirstNameOrder")
CNGivenNameFirstNameOrder = _Class("CNGivenNameFirstNameOrder")
CNReputationStore = _Class("CNReputationStore")
CNGroup = _Class("CNGroup")
CNMutableGroup = _Class("CNMutableGroup")
CNDeduplication = _Class("CNDeduplication")
CNContactKeyVector = _Class("CNContactKeyVector")
CNMutableContactKeyVector = _Class("CNMutableContactKeyVector")
CNiOSAddressBookDataMapper = _Class("CNiOSAddressBookDataMapper")
CNSocialProfile = _Class("CNSocialProfile")
CNMutableSocialProfile = _Class("CNMutableSocialProfile")
CNContactMatchSummarizer = _Class("CNContactMatchSummarizer")
CNContactImage = _Class("CNContactImage")
CNContact = _Class("CNContact")
CNMutableContact = _Class("CNMutableContact")
CNFetchResult = _Class("CNFetchResult")
CNPostalAddress = _Class("CNPostalAddress")
CNMutablePostalAddress = _Class("CNMutablePostalAddress")
CNChangeHistoryTriageLogger = _Class("CNChangeHistoryTriageLogger")
CNPerContactPropertyKeyDescriptor = _Class("CNPerContactPropertyKeyDescriptor")
CNCDAccountFetcher = _Class("CNCDAccountFetcher")
CNiOSABSaveContext = _Class("CNiOSABSaveContext")
CNContactImageStore = _Class("CNContactImageStore")
_CNChangeHistoryFetchExecutionResponse = _Class(
    "_CNChangeHistoryFetchExecutionResponse"
)
CNChangeHistoryFetchExecutor = _Class("CNChangeHistoryFetchExecutor")
CNTestSmartFetcher = _Class("CNTestSmartFetcher")
CNiOSABContactsUserDefaultsABWrapper = _Class("CNiOSABContactsUserDefaultsABWrapper")
CNSecureCodingClassSets = _Class("CNSecureCodingClassSets")
CNContactsEnvironment = _Class("CNContactsEnvironment")
CNContainerPermissions = _Class("CNContainerPermissions")
CNEmptyPeopleFetcher = _Class("CNEmptyPeopleFetcher")
CNiOSEncodedPeopleFetcher = _Class("CNiOSEncodedPeopleFetcher")
CNMultiValueUpdate = _Class("CNMultiValueUpdate")
CNMultiValueReorderUpdate = _Class("CNMultiValueReorderUpdate")
CNMultiValueSingleUpdate = _Class("CNMultiValueSingleUpdate")
CNMultiValueReplaceUpdate = _Class("CNMultiValueReplaceUpdate")
CNMultiValueRemoveUpdate = _Class("CNMultiValueRemoveUpdate")
CNMultiValueAddUpdate = _Class("CNMultiValueAddUpdate")
CNContactBufferDecoder = _Class("CNContactBufferDecoder")
CNChangeHistoryContactChange = _Class("CNChangeHistoryContactChange")
CNContactUpdate = _Class("CNContactUpdate")
CNContactMultiValueDiffUpdate = _Class("CNContactMultiValueDiffUpdate")
CNContactKeyValueUpdate = _Class("CNContactKeyValueUpdate")
CNContactHandleStringIndexer = _Class("CNContactHandleStringIndexer")
CNiOSContactFetcher = _Class("CNiOSContactFetcher")
CNiOSPersonFetcher = _Class("CNiOSPersonFetcher")
CNLaunchServicesRemoteAdapter = _Class("CNLaunchServicesRemoteAdapter")
CNContactsLogging = _Class("CNContactsLogging")
CNMockLoggerProvider = _Class("CNMockLoggerProvider")
CNUnifiedContacts = _Class("CNUnifiedContacts")
CNContactsUserDefaults = _Class("CNContactsUserDefaults")
CNContactsUserDefaultsX = _Class("CNContactsUserDefaultsX")
CNiOSABContactsUserDefaults = _Class("CNiOSABContactsUserDefaults")
CNInstantMessageAddress = _Class("CNInstantMessageAddress")
CNMutableInstantMessageAddress = _Class("CNMutableInstantMessageAddress")
CNContactImageSaveRequest = _Class("CNContactImageSaveRequest")
CNActivityAlert = _Class("CNActivityAlert")
CNMutableActivityAlert = _Class("CNMutableActivityAlert")
CNCalculatesContactDiff = _Class("CNCalculatesContactDiff")
CNChangeHistoryClearRequest = _Class("CNChangeHistoryClearRequest")
CNChangeHistoryResultEventConverter = _Class("CNChangeHistoryResultEventConverter")
CNContactsLoggerProvider = _Class("CNContactsLoggerProvider")
CNAccount = _Class("CNAccount")
CNMockSpotlightIndexingLogger = _Class("CNMockSpotlightIndexingLogger")
CNContactRelationLocalizationProvider = _Class("CNContactRelationLocalizationProvider")
CNContactRelationsDescriptionLabels = _Class("CNContactRelationsDescriptionLabels")
CNPropertyDescription = _Class("CNPropertyDescription")
CNImageHashDescription = _Class("CNImageHashDescription")
CNImageTypeDescription = _Class("CNImageTypeDescription")
CNDowntimeWhitelistDescription = _Class("CNDowntimeWhitelistDescription")
CNPreferredChannelDescription = _Class("CNPreferredChannelDescription")
CNMapsDataDescription = _Class("CNMapsDataDescription")
CNAbstractActivityAlertDescription = _Class("CNAbstractActivityAlertDescription")
CNTextAlertDescription = _Class("CNTextAlertDescription")
CNCallAlertDescription = _Class("CNCallAlertDescription")
CNPhonemeDataDescription = _Class("CNPhonemeDataDescription")
CNMultiValuePropertyDescription = _Class("CNMultiValuePropertyDescription")
CNCompoundMultiValuePropertyDescription = _Class(
    "CNCompoundMultiValuePropertyDescription"
)
CNPostalAddressesDescription = _Class("CNPostalAddressesDescription")
CNSocialProfilesDescription = _Class("CNSocialProfilesDescription")
CNInstantMessageAddressesDescription = _Class("CNInstantMessageAddressesDescription")
CNContactRelationsDescription = _Class("CNContactRelationsDescription")
CNDatesDescription = _Class("CNDatesDescription")
CNCalendarURIsDescription = _Class("CNCalendarURIsDescription")
CNUrlAddressesDescription = _Class("CNUrlAddressesDescription")
CNEmailAddressesDescription = _Class("CNEmailAddressesDescription")
CNPhoneNumbersDescription = _Class("CNPhoneNumbersDescription")
CNContactTypeDescription = _Class("CNContactTypeDescription")
CNPreferredApplePersonaIdentifierDescription = _Class(
    "CNPreferredApplePersonaIdentifierDescription"
)
CNPreferredLikenessSourceDescription = _Class("CNPreferredLikenessSourceDescription")
CNPreferredForImageDescription = _Class("CNPreferredForImageDescription")
CNPreferredForNameDescription = _Class("CNPreferredForNameDescription")
CNLinkIdentifierDescription = _Class("CNLinkIdentifierDescription")
CNImageDataAvailableDescription = _Class("CNImageDataAvailableDescription")
CNSyncImageDataDescription = _Class("CNSyncImageDataDescription")
CNFullscreenImageDataDescription = _Class("CNFullscreenImageDataDescription")
CNThumbnailImageDataDescription = _Class("CNThumbnailImageDataDescription")
CNCropRectDescription = _Class("CNCropRectDescription")
CNImageDataDescription = _Class("CNImageDataDescription")
CNNoteDescription = _Class("CNNoteDescription")
CNModificationDateDescription = _Class("CNModificationDateDescription")
CNCreationDateDescription = _Class("CNCreationDateDescription")
CNNonGregorianBirthdayDescription = _Class("CNNonGregorianBirthdayDescription")
CNBirthdayDescription = _Class("CNBirthdayDescription")
CNJobTitleDescription = _Class("CNJobTitleDescription")
CNDepartmentDescription = _Class("CNDepartmentDescription")
CNOrganizationNameDescription = _Class("CNOrganizationNameDescription")
CNSectionForSortingByFamilyNameDescription = _Class(
    "CNSectionForSortingByFamilyNameDescription"
)
CNSectionForSortingByGivenNameDescription = _Class(
    "CNSectionForSortingByGivenNameDescription"
)
CNPronunciationFamilyNameDescription = _Class("CNPronunciationFamilyNameDescription")
CNPronunciationGivenNameDescription = _Class("CNPronunciationGivenNameDescription")
CNPhoneticOrganizationNameDescription = _Class("CNPhoneticOrganizationNameDescription")
CNPhoneticFamilyNameDescription = _Class("CNPhoneticFamilyNameDescription")
CNPhoneticMiddleNameDescription = _Class("CNPhoneticMiddleNameDescription")
CNPhoneticGivenNameDescription = _Class("CNPhoneticGivenNameDescription")
CNNicknameNameDescription = _Class("CNNicknameNameDescription")
CNPreviousFamilyNameDescription = _Class("CNPreviousFamilyNameDescription")
CNNameSuffixDescription = _Class("CNNameSuffixDescription")
CNFamilyNameDescription = _Class("CNFamilyNameDescription")
CNMiddleNameDescription = _Class("CNMiddleNameDescription")
CNGivenNameDescription = _Class("CNGivenNameDescription")
CNNamePrefixDescription = _Class("CNNamePrefixDescription")
CNExternalImageURIDescription = _Class("CNExternalImageURIDescription")
CNExternalUUIDDescription = _Class("CNExternalUUIDDescription")
CNExternalModificationTagDescription = _Class("CNExternalModificationTagDescription")
CNExternalRepresentationDescription = _Class("CNExternalRepresentationDescription")
CNExternalIdentifierDescription = _Class("CNExternalIdentifierDescription")
CNIOSLegacyIdentifierDescription = _Class("CNIOSLegacyIdentifierDescription")
CNInternalIdentifierDescription = _Class("CNInternalIdentifierDescription")
CNiOSABUtilities = _Class("CNiOSABUtilities")
CNDowntimeWhitelistContainerFetcher = _Class("CNDowntimeWhitelistContainerFetcher")
CNXPCDataMapperProgressiveHandler = _Class("CNXPCDataMapperProgressiveHandler")
CNXPCDataMapper = _Class("CNXPCDataMapper")
CNFetchRequest = _Class("CNFetchRequest")
CNContactFetchRequest = _Class("CNContactFetchRequest")
CNChangeHistoryFetchRequest = _Class("CNChangeHistoryFetchRequest")
_CNFavoritesLogger = _Class("_CNFavoritesLogger")
CNContactVerifier = _Class("CNContactVerifier")
CNCalculatesMultiValueDiff = _Class("CNCalculatesMultiValueDiff")
CNContactFetchExecutor = _Class("CNContactFetchExecutor")
CNContactVCardParsedResultBuilderFactory = _Class(
    "CNContactVCardParsedResultBuilderFactory"
)
CNContactVCardParsedResultBuilder = _Class("CNContactVCardParsedResultBuilder")
CNChangeHistoryEvent = _Class("CNChangeHistoryEvent")
CNChangeHistoryDifferentMeCardEvent = _Class("CNChangeHistoryDifferentMeCardEvent")
CNChangeHistoryPreferredContactForImageEvent = _Class(
    "CNChangeHistoryPreferredContactForImageEvent"
)
CNChangeHistoryPreferredContactForNameEvent = _Class(
    "CNChangeHistoryPreferredContactForNameEvent"
)
CNChangeHistoryUnlinkContactEvent = _Class("CNChangeHistoryUnlinkContactEvent")
CNChangeHistoryLinkContactsEvent = _Class("CNChangeHistoryLinkContactsEvent")
CNChangeHistoryRemoveSubgroupFromGroupEvent = _Class(
    "CNChangeHistoryRemoveSubgroupFromGroupEvent"
)
CNChangeHistoryAddSubgroupToGroupEvent = _Class(
    "CNChangeHistoryAddSubgroupToGroupEvent"
)
CNChangeHistoryRemoveMemberFromGroupEvent = _Class(
    "CNChangeHistoryRemoveMemberFromGroupEvent"
)
CNChangeHistoryAddMemberToGroupEvent = _Class("CNChangeHistoryAddMemberToGroupEvent")
CNChangeHistoryDeleteGroupEvent = _Class("CNChangeHistoryDeleteGroupEvent")
CNChangeHistoryUpdateGroupEvent = _Class("CNChangeHistoryUpdateGroupEvent")
CNChangeHistoryAddGroupEvent = _Class("CNChangeHistoryAddGroupEvent")
CNChangeHistoryDeleteContactEvent = _Class("CNChangeHistoryDeleteContactEvent")
CNChangeHistoryUpdateContactEvent = _Class("CNChangeHistoryUpdateContactEvent")
CNChangeHistoryAddContactEvent = _Class("CNChangeHistoryAddContactEvent")
CNChangeHistoryDropEverythingEvent = _Class("CNChangeHistoryDropEverythingEvent")
CNLabeledValue = _Class("CNLabeledValue")
CNContactChangeRequest = _Class("CNContactChangeRequest")
CNClassKitServices = _Class("CNClassKitServices")
CNTCC = _Class("CNTCC")
CNGeminiManager = _Class("CNGeminiManager")
CNGeminiResult = _Class("CNGeminiResult")
CNGeminiChannel = _Class("CNGeminiChannel")
CNDateComponentsEquivalence = _Class("CNDateComponentsEquivalence")
CNContactStore = _Class("CNContactStore")
CNSuggestedContactStore = _Class("CNSuggestedContactStore")
CNDataMapperContactStore = _Class("CNDataMapperContactStore")
CNAggregateContactStore = _Class("CNAggregateContactStore")
CNContainerPropertyDescription = _Class("CNContainerPropertyDescription")
CNContainerLastSyncDateDescription = _Class("CNContainerLastSyncDateDescription")
CNContainerGuardianStateDirtyDescription = _Class(
    "CNContainerGuardianStateDirtyDescription"
)
CNContainerGuardianRestrictedDescription = _Class(
    "CNContainerGuardianRestrictedDescription"
)
CNContainerRestrictionsDescription = _Class("CNContainerRestrictionsDescription")
CNContainerMeIdentifierDescription = _Class("CNContainerMeIdentifierDescription")
CNContainerConstraintsPathDescription = _Class("CNContainerConstraintsPathDescription")
CNContainerExternalSyncDataDescription = _Class(
    "CNContainerExternalSyncDataDescription"
)
CNContainerExternalSyncTagDescription = _Class("CNContainerExternalSyncTagDescription")
CNContainerExternalModificationTagDescription = _Class(
    "CNContainerExternalModificationTagDescription"
)
CNContainerExternalIdentifierDescription = _Class(
    "CNContainerExternalIdentifierDescription"
)
CNContainerEnabledDescription = _Class("CNContainerEnabledDescription")
CNContainerAccountIdentifierDescription = _Class(
    "CNContainerAccountIdentifierDescription"
)
CNContainerIOSLegacyIdentifierDescription = _Class(
    "CNContainerIOSLegacyIdentifierDescription"
)
CNContainerTypeDescription = _Class("CNContainerTypeDescription")
CNContainerNameDescription = _Class("CNContainerNameDescription")
CNContainerIdentifierDescription = _Class("CNContainerIdentifierDescription")
CNGeminiInteraction = _Class("CNGeminiInteraction")
CNMultiValueDiff = _Class("CNMultiValueDiff")
CNiOSABContactBuffersDecoder = _Class("CNiOSABContactBuffersDecoder")
CNContactSuggestionMatch = _Class("CNContactSuggestionMatch")
CNChangeHistoryGroupChange = _Class("CNChangeHistoryGroupChange")
CNIndexRequestHandler = _Class("CNIndexRequestHandler")
CNSaveRequestVisitationTask = _Class("CNSaveRequestVisitationTask")
_CNABPredicateObservable = _Class("_CNABPredicateObservable")
CNContactImageManagedObject = _Class("CNContactImageManagedObject")
CNPredicate = _Class("CNPredicate")
CNiOSABContainerOfContactPredicate = _Class("CNiOSABContainerOfContactPredicate")
CNiOSABSocialProfileContactPredicate = _Class("CNiOSABSocialProfileContactPredicate")
CNCDAllContainersPredicate = _Class("CNCDAllContainersPredicate")
CNiOSABPreferredNameContactsPredicate = _Class("CNiOSABPreferredNameContactsPredicate")
CNiOSABEKParticipantPredicate = _Class("CNiOSABEKParticipantPredicate")
CNiOSABMapDataContactPredicate = _Class("CNiOSABMapDataContactPredicate")
CNiOSABGroupNameMatchingPredicate = _Class("CNiOSABGroupNameMatchingPredicate")
CNiOSABLocalContainerPredicate = _Class("CNiOSABLocalContainerPredicate")
CNiOSABGroupIdentifiersPredicate = _Class("CNiOSABGroupIdentifiersPredicate")
CNiOSABGroupiOSLegacyIdentifierPredicate = _Class(
    "CNiOSABGroupiOSLegacyIdentifierPredicate"
)
CNContactsWithIdentifiersPredicate = _Class("CNContactsWithIdentifiersPredicate")
CNiOSABContactIdentifiersPredicate = _Class("CNiOSABContactIdentifiersPredicate")
CNiOSABLabeledValueContactPredicate = _Class("CNiOSABLabeledValueContactPredicate")
CNInstantMessageAddressContactPredicate = _Class(
    "CNInstantMessageAddressContactPredicate"
)
CNiOSABOrganizationNameContactPredicate = _Class(
    "CNiOSABOrganizationNameContactPredicate"
)
CNiOSABContactLegacyIdentifierPredicate = _Class(
    "CNiOSABContactLegacyIdentifierPredicate"
)
CNiOSABPreferredNameInContainersAndGroupsPredicate = _Class(
    "CNiOSABPreferredNameInContainersAndGroupsPredicate"
)
CNiOSABPreferredChannelContactPredicate = _Class(
    "CNiOSABPreferredChannelContactPredicate"
)
CNiOSABPostalAddressContactPredicate = _Class("CNiOSABPostalAddressContactPredicate")
CNiOSABContainersForAccountExternalIdentifierPredicate = _Class(
    "CNiOSABContainersForAccountExternalIdentifierPredicate"
)
CNiOSABContainerIdentifiersPredicate = _Class("CNiOSABContainerIdentifiersPredicate")
CNPhoneNumberContactPredicate = _Class("CNPhoneNumberContactPredicate")
CNiOSABPhoneNumberContactPredicate = _Class("CNiOSABPhoneNumberContactPredicate")
CNiOSABContaineriOSLegacyIdentifierPredicate = _Class(
    "CNiOSABContaineriOSLegacyIdentifierPredicate"
)
CNiOSABContactsInGroupPredicate = _Class("CNiOSABContactsInGroupPredicate")
CNiOSABGroupsInGroupPredicate = _Class("CNiOSABGroupsInGroupPredicate")
CNPostalAddressContactPredicate = _Class("CNPostalAddressContactPredicate")
CNiOSABAllContactsPredicate = _Class("CNiOSABAllContactsPredicate")
CNiOSABURLContactPredicate = _Class("CNiOSABURLContactPredicate")
CNiOSABDisabledContainersPredicate = _Class("CNiOSABDisabledContainersPredicate")
CNiOSABStringMatchContactPredicate = _Class("CNiOSABStringMatchContactPredicate")
CNiOSABAccountForExternalIdentifierPredicate = _Class(
    "CNiOSABAccountForExternalIdentifierPredicate"
)
CNContactWithNamePredicate = _Class("CNContactWithNamePredicate")
CNiOSABContactWithNamePredicate = _Class("CNiOSABContactWithNamePredicate")
CNiOSABContainerOfGroupPredicate = _Class("CNiOSABContainerOfGroupPredicate")
CNHandleStringsContactPredicate = _Class("CNHandleStringsContactPredicate")
CNiOSABHandleStringsContactPredicate = _Class("CNiOSABHandleStringsContactPredicate")
CNiOSABContainersForAccountPredicate = _Class("CNiOSABContainersForAccountPredicate")
CNiOSABAccountForContainerPredicate = _Class("CNiOSABAccountForContainerPredicate")
CNContainerIdentifiersPredicate = _Class("CNContainerIdentifiersPredicate")
CNiOSABGroupsInContainerPredicate = _Class("CNiOSABGroupsInContainerPredicate")
CNiOSABDefaultContainerForAccountPredicate = _Class(
    "CNiOSABDefaultContainerForAccountPredicate"
)
CNEmailAddressContactPredicate = _Class("CNEmailAddressContactPredicate")
CNiOSABEmailAddressContactPredicate = _Class("CNiOSABEmailAddressContactPredicate")
CNLinkedContactsPredicate = _Class("CNLinkedContactsPredicate")
CNiOSABLinkedContactsPredicate = _Class("CNiOSABLinkedContactsPredicate")
CNSocialProfileContactPredicate = _Class("CNSocialProfileContactPredicate")
CNMeContactsPredicate = _Class("CNMeContactsPredicate")
CNiOSABMeContactsPredicate = _Class("CNiOSABMeContactsPredicate")
CNSuggestedContactIdentifierPredicate = _Class("CNSuggestedContactIdentifierPredicate")
CNiOSABAccountIdentifiersPredicate = _Class("CNiOSABAccountIdentifiersPredicate")
CNiOSABContactsInContainerPredicate = _Class("CNiOSABContactsInContainerPredicate")
CNFullTextSearchContactPredicate = _Class("CNFullTextSearchContactPredicate")
CNiOSABFullTextSearchContactPredicate = _Class("CNiOSABFullTextSearchContactPredicate")
CNiOSABFaultFulfillmentPredicate = _Class("CNiOSABFaultFulfillmentPredicate")
CNiOSABInstantMessageAddressContactPredicate = _Class(
    "CNiOSABInstantMessageAddressContactPredicate"
)
CNChangeHistoryResultEnumerator = _Class("CNChangeHistoryResultEnumerator")
CNPostalAddressFormatter = _Class("CNPostalAddressFormatter")
CNContactSearchIndexFormatter = _Class("CNContactSearchIndexFormatter")
CNContactFormatter = _Class("CNContactFormatter")
